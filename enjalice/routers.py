from typing import Optional, Callable, List, Awaitable, TypeVar
from itertools import zip_longest

from ._hints import MessageHandlerFunction
from .exceptions import HandlerTypeError
from .intent_handler import IntentHandler, IntentHandlersCollection
from .request import AliceRequest
from .response import AliceResponse
from . import context
from .exceptions import NoHandler


T = TypeVar('T')


class Blueprint:
    """Base class implements intent routing logic.

    Can be used to declare intents in a modular way.
    """

    def __init__(self):
        self.intents: IntentHandlersCollection = IntentHandlersCollection()

    def _recreate(self: T) -> T:
        """Return exact copy of this blueprint, without handlers
        """
        return Blueprint()

    def register_message_handler(self,
                                 priority: int,
                                 intent: Optional[str],
                                 handler: Callable):
        intent_handler = IntentHandler(
            name=intent,
            priority=priority,
            handler=handler
        )
        self.intents.add(intent_handler)

    def message_handler(self, priority: int,
                        intent: Optional[List[str]] = None):
        def decorator(callback):
            if intent:
                for intent_name in intent:
                    self.register_message_handler(priority=priority,
                                                  intent=intent_name,
                                                  handler=callback)
            else:
                self.register_message_handler(priority=priority,
                                              intent=None,
                                              handler=callback)
            return callback

        return decorator

    async def _get_response(self,
                            handler: MessageHandlerFunction,
                            request: AliceRequest
                            ) -> Optional[AliceResponse]:
        responder = handler(request)
        # Handle async functions
        if isinstance(responder, Awaitable):
            response = await responder

        # Handle sync functions
        elif responder is None or isinstance(responder, AliceResponse):
            response = responder

        else:
            raise HandlerTypeError(f'Handler returned: {responder}')

        return response

    async def _send_start_message(self, request_obj: AliceRequest):
        raise NotImplementedError   # Blueprint does not implement start message

    async def dispatch_request(self, request_obj: AliceRequest) -> AliceResponse:
        context.session_state.set(request_obj.state.session)

        response = None

        if request_obj.session.new:
            # When user starts a new conversation
            response = await self._send_start_message(request_obj)
        else:
            for intent_handler in self.intents.iter_intents(
                    request_obj.request.nlu.intents
            ):
                response = await self._get_response(intent_handler.handler,
                                                    request_obj)
                if response is not None:
                    break

        if response is None:
            raise NoHandler(f"Can't handle request: {request_obj}")

        return response

    def register_blueprint(self, bp: 'Blueprint'):
        self += bp

    def __iadd__(self: T, other) -> T:
        if not isinstance(other, Blueprint):
            return NotImplemented
        for intent in other.intents:
            self.intents.add(intent)
        return self

    def __add__(self: T, other) -> T:
        if not isinstance(other, Blueprint):
            return NotImplemented

        bp = self._recreate()
        for intent1, intent2 in zip_longest(other.intents, self.intents):
            if intent1 is not None:
                bp.intents.add(intent1)
            if intent2 is not None:
                bp.intents.add(intent2)
        return bp


class Dispatcher(Blueprint):
    """A Blueprint that also implements start message

    Use as main intent router in your app.
    """

    def __init__(self, start_handler: MessageHandlerFunction):
        self.start_handler = start_handler
        super().__init__()

    def _recreate(self: T) -> T:
        return self.__class__(self.start_handler)

    async def _send_start_message(self, request_obj: AliceRequest):
        return await self._get_response(self.start_handler, request_obj)

from typing import Optional, List, Callable, Awaitable

from . import context
from ._hints import MessageHandlerFunction
from .exceptions import NoHandler, HandlerTypeError
from .intent_handler import IntentHandlersCollection, IntentHandler
from .request import AliceRequest
from .response import AliceResponse


class Dispatcher:

    def __init__(self, start_handler: MessageHandlerFunction):
        self.intents: IntentHandlersCollection = \
            IntentHandlersCollection()

        self.start_dialog_handler = start_handler

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

    def start_handler(self):
        def decorator(callback):
            if isinstance(callback, Callable):
                self.start_dialog_handler = callback
            else:
                raise HandlerTypeError
            return callback

        return decorator

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

    async def dispatch_request(self, request_obj: AliceRequest) -> AliceResponse:
        """Process single AliceRequest, return an AliceResponse

        raises NoHandler if all handlers returned None
        """
        context.session_state.set(request_obj.state.session)

        response = None

        if request_obj.session.new:
            # When user starts a new conversation
            response = await self._get_response(self.start_dialog_handler, request_obj)
        else:
            intents = filter(
                lambda i: any([i.name in request_obj.request.nlu.intents,
                               i.name is None]),
                self.intents
            )
            for intent_handler in intents:
                response = await self._get_response(intent_handler.handler,
                                                    request_obj)
                if response is not None:
                    break

        if response is None:
            raise NoHandler(f"Can't handle request: {request_obj}")

        return response

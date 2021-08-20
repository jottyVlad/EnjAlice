from typing import Optional, List, Callable, Awaitable

from .consts import DEFAULT_START_TEXT
from .intent_handler import IntentHandlersCollection, IntentHandler
from .request import AliceRequest
from .response import AliceResponse
from .exceptions import NoHandler, HandlerTypeError


class Dispatcher:
    def __init__(self):
        self.intents: IntentHandlersCollection = \
            IntentHandlersCollection()

        self.start_text: str = DEFAULT_START_TEXT

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

    async def dispatch_request(self, request_obj: AliceRequest) -> AliceResponse:
        """Process single AliceRequest, return an AliceResponse

        raises NoHandler if all handlers returned None
        """
        if request_obj.session.new:
            # When user starts a new conversation
            response = AliceResponse()
            response.response.text = self.dispatcher.start_text
            return response

        for intent_handler in self.intents:
            if (intent_handler.name in request_obj.request.nlu.intents)\
                    or intent_handler.name is None:
                alice_response = AliceResponse()
                alice_response.session_state = request_obj.state.session
                responder = intent_handler.handler(
                    request_obj,
                    alice_response
                )

                if isinstance(responder, Awaitable):   # Handle async functions
                    response = await responder
                elif responder is None or isinstance(responder, AliceResponse):  # Handle sync functions
                    response = responder
                else:
                    raise HandlerTypeError(f'Handler returned: {responder}')
                if response is None:
                    continue

                return response

        raise NoHandler(f"Can't handle request: {request_obj}")

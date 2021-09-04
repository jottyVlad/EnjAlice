from abc import ABC, abstractmethod
from typing import Optional, Callable, List, Awaitable

from .._hints import MessageHandlerFunction
from ..exceptions import HandlerTypeError
from ..intent_handler import IntentHandler, IntentHandlersCollection
from ..request import AliceRequest
from ..response import AliceResponse


class ABCRoute(ABC):
    @abstractmethod
    def __init__(self):
        self.intents: IntentHandlersCollection = NotImplemented

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

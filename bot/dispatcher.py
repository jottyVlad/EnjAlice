from typing import Optional, List, Coroutine

from bot.consts import DEFAULT_START_TEXT
from bot.intent_handler import IntentHandlersCollection, IntentHandler


class Dispatcher:
    def __init__(self):
        self.intents: IntentHandlersCollection[IntentHandler] = \
            IntentHandlersCollection([])

        self.start_text: str = DEFAULT_START_TEXT

    def set_start_text(self, text: str):
        self.start_text = text

    def register_message_handler(self,
                                 priority: int,
                                 intent: Optional[str],
                                 handler: Coroutine):
        intent_handler = IntentHandler(
                        name=intent,
                        priority=priority,
                        handler=handler
                    )
        self.intents.append(intent_handler)

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

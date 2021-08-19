from bot.consts import DEFAULT_START_TEXT
from bot.intent_handler import IntentHandlersCollection, IntentHandler


class Dispatcher:
    def __init__(self):
        self.intents: IntentHandlersCollection[IntentHandler] = \
            IntentHandlersCollection([])

        self.start_text: str = DEFAULT_START_TEXT

    def set_start_text(self, text: str):
        self.start_text = text

    def message_handler(self, priority: int,
                        intent: str):
        def decorator(callback):
            intent_handler = IntentHandler(
                name=intent,
                priority=priority,
                handler=callback
            )
            self.intents.append(intent_handler)
            return callback
        return decorator

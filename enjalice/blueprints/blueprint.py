from enjalice.intent_handler import IntentHandlersCollection
from enjalice.internals.route import ABCRoute


class Blueprint(ABCRoute):
    def __init__(self):
        self.intents: IntentHandlersCollection = \
            IntentHandlersCollection()

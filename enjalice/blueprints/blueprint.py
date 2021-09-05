from enjalice.intent_handler import IntentHandlersCollection
from enjalice.internals.route import ABCRoute


class Blueprint(ABCRoute):
    def __init__(self):
        self.intents: IntentHandlersCollection = \
            IntentHandlersCollection()

    def add(self, obj: "Blueprint"):
        if not isinstance(obj, Blueprint):
            raise AttributeError("Attribute must be blueprint")

        for intent in obj.intents:
            self.intents.add(intent)

        return self

    def __add__(self, other):
        self.add(other)
        return self

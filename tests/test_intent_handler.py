from random import randint
from time import sleep
from secrets import token_hex

import pytest

from enjalice.intent_handler import IntentHandler, IntentHandlersCollection


COLLECTION_SIZE = 16


@pytest.fixture
def collection():
    c = IntentHandlersCollection()
    handler = lambda: "dummy"
    for i in range(COLLECTION_SIZE):
        c.add(
            IntentHandler(
                handler=handler,
                name=f"dummy_{token_hex(8)}",
                priority=randint(0, 100)
            )
        )
    return c


def test_order(collection: IntentHandlersCollection):
    last_priority = float("inf")
    for handler in collection:
        assert last_priority >= handler.priority, "Order in IntentHandlersCollection is BROKEN"
        last_priority = handler.priority


def test_contains(collection: IntentHandlersCollection):
    for i in collection:
        assert i in collection, "__contains__ method of IntentHandlersCollection is BROKEN"


def test_discard(collection: IntentHandlersCollection):
    for i in collection:
        collection.discard(i)
        assert i not in collection, "discard method of IntentHandlersCollection is BROKEN"


def test_len(collection: IntentHandlersCollection):
    assert len(collection) == COLLECTION_SIZE

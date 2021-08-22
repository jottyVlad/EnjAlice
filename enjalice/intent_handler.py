from bisect import insort
from collections.abc import MutableSet
from contextlib import suppress
from typing import Iterator, Optional

from pydantic import BaseModel

from ._hints import MessageHandlerFunction


class IntentHandler(BaseModel):
    name: Optional[str]
    priority: int
    handler: MessageHandlerFunction

    def __lt__(self, other: "IntentHandler") -> bool:
        if not isinstance(other, IntentHandler):
            return NotImplemented
        return self.priority < other.priority

    def __gt__(self, other: "IntentHandler") -> bool:
        if not isinstance(other, IntentHandler):
            return NotImplemented
        return self.priority > other.priority


class IntentHandlersCollection(MutableSet[IntentHandler]):
    def __init__(self) -> None:
        self.__list_of_handlers = []

    def add(self, obj: IntentHandler) -> None:
        """Add given IntentHandler to collection
        """
        assert isinstance(obj, IntentHandler)
        insort(self.__list_of_handlers, obj)

    def __contains__(self, obj: IntentHandler) -> bool:
        assert isinstance(obj, IntentHandler)
        return obj in self.__list_of_handlers

    def __iter__(self) -> Iterator[IntentHandler]:
        return reversed(self.__list_of_handlers)

    def __len__(self):
        return len(self.__list_of_handlers)

    def discard(self, obj: IntentHandler):
        """Remove given IntentHandler from collection if it exists
        """
        assert isinstance(obj, IntentHandler)
        with suppress(ValueError):
            self.__list_of_handlers.pop(self.__list_of_handlers.index(obj))

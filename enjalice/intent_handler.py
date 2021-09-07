import dataclasses
from bisect import insort
from collections import defaultdict
from collections.abc import MutableSet
from contextlib import suppress
from itertools import zip_longest
from typing import Iterator, Optional, Iterable, Dict, List

from ._hints import MessageHandlerFunction


@dataclasses.dataclass
class IntentHandler:
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
        self.__handlers: Dict[Optional[str], List[IntentHandler]] = defaultdict(list)

    def add(self, obj: IntentHandler) -> None:
        """Add given IntentHandler to collection
        """
        assert isinstance(obj, IntentHandler)
        insort(self.__handlers[obj.name], obj)

    def __contains__(self, obj: IntentHandler) -> bool:
        assert isinstance(obj, IntentHandler)
        return any(obj in b for b in self.__handlers.values())

    def __iter__(self) -> Iterator[IntentHandler]:
        buckets = map(reversed, self.__handlers.values())
        for batch in zip_longest(*buckets):
            for handler in sorted(filter(lambda i: i is not None, batch), reverse=True):
                yield handler

    def __len__(self):
        # TODO doesnt actually count number of unique handlers
        return sum(map(len, self.__handlers.values()))

    def iter_intents(self,
                     intents: Iterable[str],
                     allow_fallback=True
                     ) -> Iterator[IntentHandler]:
        intent_buckets = [self.__handlers[i] for i in intents]
        if allow_fallback:
            intent_buckets.append(self.__handlers[None])
        for batch in zip_longest(*intent_buckets):
            for handler in sorted(filter(lambda i: i is not None, batch)):
                yield handler

    def discard(self, obj: IntentHandler):
        """Remove given IntentHandler from collection if it exists
        """
        assert isinstance(obj, IntentHandler)
        for i in self.__handlers.values():
            with suppress(ValueError):
                i.remove(obj)

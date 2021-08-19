import dataclasses
from typing import Coroutine, List


@dataclasses.dataclass
class IntentHandler:
    name: str
    priority: int
    handler: Coroutine


class IntentHandlersCollection(list):
    def sort_by_priority(self):
        self.sort(key=lambda handler: handler.priority)

    def append(self, obj) -> None:
        super().append(obj)
        self.sort_by_priority()

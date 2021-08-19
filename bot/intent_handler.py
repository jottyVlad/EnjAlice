from typing import Callable

from pydantic import BaseModel


class IntentHandler(BaseModel):
    name: str
    priority: int
    handler: Callable


class IntentHandlersCollection(list):
    def priority_sort(self):
        self.sort(key=lambda handler: handler.priority, reverse=True)

    def append(self, obj) -> None:
        super().append(obj)
        self.priority_sort()

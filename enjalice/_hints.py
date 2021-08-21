from typing import Callable, Awaitable, Optional, Union

from .response import AliceResponse


HandlerResult = Optional[AliceResponse]


MessageHandlerFunction = Callable[
    ...,
    Union[
        HandlerResult,
        Awaitable[HandlerResult]
    ]
]

StartDialogHandlerFunction = Callable
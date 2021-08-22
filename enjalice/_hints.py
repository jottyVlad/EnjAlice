from typing import Callable, Awaitable, Optional, Union

from .request import AliceRequest
from .response import AliceResponse

HandlerResult = Optional[AliceResponse]

MessageHandlerFunction = Callable[
    [AliceRequest],
    Union[
        HandlerResult,
        Awaitable[HandlerResult]
    ]
]

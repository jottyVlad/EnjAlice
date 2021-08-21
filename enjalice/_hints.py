from typing import Callable, Awaitable, Optional, Union

from .response import AliceResponse
from .request import AliceRequest


HandlerResult = Optional[AliceResponse]


MessageHandlerFunction = Callable[
    [AliceRequest],
    Union[
        HandlerResult,
        Awaitable[HandlerResult]
    ]
]

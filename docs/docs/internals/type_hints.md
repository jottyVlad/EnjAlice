# Type Hints

- `HandlerResult = Optional[AliceResponse]`
- 
```
  MessageHandlerFunction = Callable[
    [AliceRequest],
    Union[
        HandlerResult,
        Awaitable[HandlerResult]
    ] 
]
```
- `CT = TypeVar('CT', bound=Card)`
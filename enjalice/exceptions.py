class NoHandler(RuntimeError):
    """Exception raised when none of message
    handlers have returned a response for given request
    """


class HandlerTypeError(TypeError):
    """Exception raised when message handler returns wrong type
    """

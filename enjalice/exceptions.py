class NoHandler(RuntimeError):
    """Exception raised when none of message
    handlers have returned a response for given request
    """

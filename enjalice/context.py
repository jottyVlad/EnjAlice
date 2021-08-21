from typing import Dict, Any, Optional
from contextvars import ContextVar

session_state: ContextVar[Optional[Dict[str, Any]]] = ContextVar('session', default=None)

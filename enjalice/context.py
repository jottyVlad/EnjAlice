from contextvars import ContextVar
from typing import Dict, Any, Optional

session_state: ContextVar[Optional[Dict[str, Any]]] = ContextVar('session', default=None)

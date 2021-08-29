from contextvars import ContextVar
from typing import Dict, Any, Optional

session_state: ContextVar[Optional[Dict[str, Any]]] = ContextVar('session', default=None)


def get_session_state() -> Dict:
    """Get current session from context or empty dict
    """
    session = session_state.get()
    return session.copy() if session else dict()

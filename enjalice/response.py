from typing import Dict, Optional

from pydantic import BaseModel, Field

from . import context


def get_session_state() -> Dict:
    """Get current session from context or empty dict
    """
    session = context.session_state.get()
    return session.copy() if session else dict()


class Response(BaseModel):
    text: str = ""
    tts: Optional[str] = ""
    end_session: bool = False


class AliceResponse(BaseModel):
    response: Response = Field(default_factory=Response)
    session_state: Dict = Field(default_factory=get_session_state)
    version: str = "1.0"


def text(msg: str, tts: str = "", end_session: bool = False) -> AliceResponse:
    """Create new AliceResponse from text
    """
    r = AliceResponse()
    r.response.text = msg
    r.response.tts = tts
    r.response.end_session = end_session
    return r

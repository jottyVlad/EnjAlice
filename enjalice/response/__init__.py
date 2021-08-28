from typing import Dict

from pydantic import BaseModel, Field

from .response import Response, get_session_state


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

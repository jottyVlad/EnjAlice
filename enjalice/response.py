from typing import Dict, Optional

from pydantic import BaseModel, Field


class Response(BaseModel):
    text: str = ""
    tts: Optional[str] = ""
    end_session: bool = False


class AliceResponse(BaseModel):
    response: Response = Response()
    session_state: Dict = Field(default_factory=dict)
    version: str = "1.0"

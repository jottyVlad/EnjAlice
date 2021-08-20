from typing import Dict

from pydantic import BaseModel, Field


class Response(BaseModel):
    text: str = ""
    end_session: bool = False


class AliceResponse(BaseModel):
    response: Response = Response()
    session_state: Dict = Field(default_factory=dict)
    version: str = "1.0"

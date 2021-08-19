from typing import Dict

from pydantic import BaseModel


class Response(BaseModel):
    text: str = ""
    end_session: bool = False


class AliceResponse(BaseModel):
    response: Response = Response()
    session_state: Dict = {}
    version: str = "1.0"

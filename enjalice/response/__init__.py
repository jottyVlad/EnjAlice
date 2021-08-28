from typing import Dict, Optional

from pydantic import BaseModel, Field

from .response import Response
from ..context import get_session_state
from .response_models import Analytics


class AliceResponse(BaseModel):
    response: Response = Field(default_factory=Response)
    analytics: Optional[Analytics]
    session_state: Dict = Field(default_factory=get_session_state)
    version: str = "1.0"

    def add_custom_sound(self, skill_id: str, sound_id: str):
        """
        Добавляет кастомное аудио к текущему tts
        :param skill_id: ID навыка
        :param sound_id: ID аудиофайла
        :return: AliceResponse (self)
        """

        self.response.tts += \
            f" <speaker audio='dialogs-upload/{skill_id}/{sound_id}.opus'> "
        return self


def text(msg: str, tts: str = "", end_session: bool = False) -> AliceResponse:
    """Create new AliceResponse from text
    """
    r = AliceResponse()
    r.response.text = msg
    r.response.tts = tts
    r.response.end_session = end_session
    return r

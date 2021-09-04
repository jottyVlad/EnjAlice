from typing import Dict, Optional

from pydantic import BaseModel, Field

from .response import Response
from .response_models import Analytics, VoiceEffects
from ..context import get_session_state


class AliceResponse(BaseModel):
    response: Response = Field(default_factory=Response)
    analytics: Optional[Analytics]
    session_state: Dict = Field(default_factory=get_session_state)
    application_state: Dict = Field(default_factory=dict)
    user_state_update: Dict = Field(default_factory=dict)
    version: str = "1.0"

    def add_custom_sound(self, skill_id: str, sound_id: str):
        """
        Добавляет кастомное аудио к текущему tts
        :param skill_id: ID навыка
        :param sound_id: ID аудиофайла
        :return: self
        """

        if not (isinstance(skill_id, str) and isinstance(sound_id, str)):
            raise AttributeError("skill_id and sound_id must be str")
        self.response.tts += \
            f" <speaker audio='dialogs-upload/{skill_id}/{sound_id}.opus'> "
        return self

    def add_voice_effect(self, effect: VoiceEffects, text: str):
        """
        Добавляет текст с эффектом к текущему tts
        :param effect: Эффект из перечисления VoiceEffects
        :param text: Текст
        :return: self
        """

        if not isinstance(text, str):
            raise AttributeError("text must be str")
        self.response.tts += \
            f"<speaker effect={effect}>{text} <speaker effect='-'>"
        return self

    def add_pause(self, ms: int):
        """
        Добавляет паузу к текущему tts
        :param ms: Длительность паузы (в миллисекундах)
        :return: self
        """

        if not isinstance(ms, int):
            raise AttributeError("ms must be int")
        self.response.tts += \
            f"sil <[{ms}]>"
        return self


def text(msg: str, tts: str = "", end_session: bool = False) -> AliceResponse:
    """Create new AliceResponse from text
    """
    r = AliceResponse()
    r.response.text = msg
    r.response.tts = tts
    r.response.end_session = end_session
    return r

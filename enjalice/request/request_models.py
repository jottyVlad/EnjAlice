from enum import Enum
from typing import Dict, Optional, List, Union

from pydantic import BaseModel, Field


class Interfaces(BaseModel):
    screen: Dict = Field(default_factory=dict)
    account_linking: Dict = Field(default_factory=dict)
    payments: Dict = Field(default_factory=dict)
    audio_player: Dict = Field(default_factory=dict)


class EntityToken(BaseModel):
    start: int
    end: int


class Entity(BaseModel):
    tokens: EntityToken = Field(default_factory=EntityToken)
    type: str = ''
    value: Union[int, Dict] = Field(default_factory=dict)


class Nlu(BaseModel):
    tokens: List[str] = Field(default_factory=list)
    entities: List[Entity] = Field(default_factory=list)
    intents: Dict[str, Dict] = Field(default_factory=dict)


class Meta(BaseModel):
    locale: str = ''
    timezone: str = ''
    client_id: str = ''
    interfaces: Interfaces = Field(default_factory=Interfaces)


class Request(BaseModel):
    command: str = ''
    original_utterance: str = ''
    type: str = ''
    nlu: Nlu = Field(default_factory=Nlu)


class User(BaseModel):
    user_id: Optional[str] = None
    access_token: str = ""


class Application(BaseModel):
    application_id: str = ''


class Session(BaseModel):
    message_id: Optional[int] = None
    session_id: str = ''
    skill_id: str = ''
    user_id: str = ''
    application: Application = Field(default_factory=Application)
    user: User = Field(default_factory=User)
    new: bool = False


class State(BaseModel):
    session: Dict = Field(default_factory=dict)
    user: Dict = Field(default_factory=dict)
    application: Dict = Field(default_factory=dict)


class Markup(BaseModel):
    dangerous_context: bool = Field(default=False)


class ShowTypes(str, Enum):
    MORNING = "MORNING"

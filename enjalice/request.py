from typing import Dict, Union, List, Optional

from pydantic import BaseModel, Field


class Interfaces(BaseModel):
    screen: Dict = Field(default_factory=dict)
    account_linking: Dict = Field(default_factory=dict)


class Entity(BaseModel):
    tokens: Dict[str, int] = Field(default_factory=dict)
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
    interfaces: Dict = Field(default_factory=dict)


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


class AliceRequest(BaseModel):
    request: Request = Field(default_factory=Request)
    meta: Meta = Field(default_factory=Meta)
    session: Session = Field(default_factory=Session)
    state: State = Field(default_factory=State)
    version: str = '1.0'

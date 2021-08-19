from typing import Dict, Union, List

from pydantic import BaseModel


class Interfaces(BaseModel):
    screen: Dict = {}
    account_linking: Dict = {}


class Entity(BaseModel):
    tokens: Dict[str, int] = {}
    type: str = ''
    value: Union[int, Dict] = {}


class Nlu(BaseModel):
    tokens: List[str] = []
    entities: List[Entity] = []
    intents: Dict[str, Dict] = {}


class Meta(BaseModel):
    locale: str = ''
    timezone: str = ''
    client_id: str = ''
    interfaces: Dict = {}


class Request(BaseModel):
    command: str = ''
    original_utterance: str = ''
    type: str = ''
    nlu: Nlu = Nlu()


class User(BaseModel):
    user_id: str = None
    access_token: str = ""


class Application(BaseModel):
    application_id: str = ''


class Session(BaseModel):
    message_id: int = None
    session_id: str = ''
    skill_id: str = ''
    user_id: str = ''
    application: Application = Application()
    user: User = User()
    new: bool = False


class State(BaseModel):
    session: Dict = {}
    user: Dict = {}
    application: Dict = {}


class AliceRequest(BaseModel):
    request: Request = Request()
    meta: Meta = Meta()
    session: Session = Session()
    state: State = State()
    version: str = '1.0'

from typing import Literal, Dict

from pydantic import BaseModel, Field

from .request_models import Nlu, Markup, ShowTypes


class SimpleUtterance(BaseModel):
    type: Literal["SimpleUtterance"] = "SimpleUtterance"
    command: str = ''
    original_utterance: str = ''
    nlu: Nlu = Field(default_factory=Nlu)
    markup: Markup = Field(default_factory=Markup)


class ButtonPressed(BaseModel):
    type: Literal["ButtonPressed"] = "ButtonPressed"
    tokens: Dict = Field(default_factory=dict)
    payload: Dict = Field(default_factory=dict)
    nlu: Nlu = Field(default_factory=Nlu)
    markup: Markup = Field(default_factory=Markup)


class PurchaseConfirmation(BaseModel):
    type: Literal["Purchase.Confirmation"] = "Purchase.Confirmation"
    purchase_request_id: str = ''
    purchase_token: str = ''
    order_id: str = ''
    purchase_timestamp: int
    purchase_payload: Dict = Field(default_factory=Dict)
    signed_data: str = ''
    signature: str = ''


class ShowPull(BaseModel):
    type: Literal["Show.Pull"] = "Show.Pull"
    show_type: ShowTypes = ShowTypes.MORNING

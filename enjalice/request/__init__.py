from typing import Union

from pydantic import BaseModel, Field

from .request_models import Meta, Session, State
from .request_types import SimpleUtterance, \
    ButtonPressed, \
    PurchaseConfirmation, \
    ShowPull


class AliceRequest(BaseModel):
    request: Union[
        SimpleUtterance,
        ButtonPressed,
        PurchaseConfirmation,
        ShowPull
    ]
    meta: Meta = Field(default_factory=Meta)
    session: Session = Field(default_factory=Session)
    state: State = Field(default_factory=State)
    version: str = '1.0'

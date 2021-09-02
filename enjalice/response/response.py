from typing import Optional, Generic, List, TypeVar, Union

from pydantic import BaseModel, Field

from enjalice.attachments.button import ResponseButton
from enjalice.attachments.cards import Card
from .response_models import DirectiveStartPurchase, \
    DirectiveConfirmPurchase, ShowItemMeta

CT = TypeVar('CT', bound=Card)


class Response(BaseModel, Generic[CT]):
    text: str = ""
    tts: Optional[str] = ""
    card: Optional[CT]
    buttons: List[ResponseButton] = Field(default_factory=list)
    directives: Optional[Union[
        DirectiveStartPurchase,
        DirectiveConfirmPurchase
    ]]
    end_session: bool = False
    show_item_meta: Optional[ShowItemMeta]

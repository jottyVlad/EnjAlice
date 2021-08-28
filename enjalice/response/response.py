from typing import Dict, Optional, Generic, List, TypeVar, Union

from pydantic import BaseModel, Field

from enjalice import context
from enjalice.attachments.button import ResponseButton
from enjalice.attachments.cards import Card
from .response_models import DirectiveStartPurchase, \
    DirectiveConfirmPurchase

CT = TypeVar('CT', bound=Card)


def get_session_state() -> Dict:
    """Get current session from context or empty dict
    """
    session = context.session_state.get()
    return session.copy() if session else dict()


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

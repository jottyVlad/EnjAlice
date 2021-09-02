import secrets
from enum import Enum
from typing import Optional, Dict, List

from pydantic import BaseModel, Field


class Currency(str, Enum):
    RUB = "RUB"


class PurchaseType(str, Enum):
    BUY = "BUY"


class NdsType(str, Enum):
    nds_20 = "nds_20"
    nds_10 = "nds_10"
    nds_0 = "nds_0"
    nds_none = "nds_none"


class Product(BaseModel):
    product_id: str
    title: str
    user_price: float
    price: float
    nds_type: NdsType
    quantity: float


class DirectiveStartPurchase(BaseModel):
    purchase_request_id: str = Field(
        default_factory=secrets.token_hex(20)
    )
    image_url: Optional[str]
    caption: str
    description: str
    currency: Currency
    type: PurchaseType
    payload: Dict = Field(default_factory=dict)
    merchant_key: str
    test_payment: bool = Field(default=False)
    products: List[Product] = Field(default_factory=list)


class DirectiveConfirmPurchase(BaseModel):
    confirm_purchase: Dict = Field(default_factory=dict)


class Event(BaseModel):
    name: str
    value: Optional[Dict]


class Analytics(BaseModel):
    events: List[Event]


class ShowItemMeta(BaseModel):
    """
    ShowItemMeta - модель для поля show_item_meta в Response (утреннее шоу Алисы)
    """
    content_id: str
    title: Optional[str]
    title_tts: Optional[str]
    publication_date: str
    expiration_date: str


class VoiceEffects(str, Enum):
    """
    Перечисление доступных голосовых эффектов. \n
    https://yandex.ru/dev/dialogs/alice/doc/speech-effects.html

    Доступные значения:

    behind_the_wall - голос из-за стены \n
    hamster — голос хомяка \n
    megaphone — голос через мегафон \n
    pitch_down — низкий голос \n
    psychodelic — психоделический голос \n
    pulse — голос с прерываниями \n
    train_announce — громкоговоритель на вокзале
    """
    behind_the_wall = "behind_the_wall"
    hamster = "hamster"
    megaphone = "megaphone"
    pitch_down = "pitch_down"
    psychodelic = "psychodelic"
    pulse = "pulse"
    train_announce = "train_announce"

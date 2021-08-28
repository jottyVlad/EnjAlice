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

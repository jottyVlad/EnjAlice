from typing import List, Optional, Literal

from pydantic import BaseModel, Field

from .button import ImageButton
from .image import ImageWithButton, ImageWithoutButton
from .items_list_addition import Header, Footer


class Card(BaseModel):
    type: str


class BigImage(Card):
    type: Literal["BigImage"] = "BigImage"
    image_id: str
    title: Optional[str]
    description: Optional[str]
    button: Optional[ImageButton] = Field(default_factory=ImageButton)


class ItemsList(Card):
    type: Literal["ItemsList"] = "ItemsList"
    header: Optional[Header] = Field(default_factory=Header)
    items: List[ImageWithButton] = Field(default_factory=list)
    footer: Optional[Footer] = Field(default_factory=Footer)


class ImageGallery(Card):
    type: Literal["ImageGallery"] = "ImageGallery"
    items: List[ImageWithoutButton] = Field(default_factory=list)

from typing import Optional

from pydantic import BaseModel, Field

from .button import ImageButton


class ImageWithButton(BaseModel):
    image_id: Optional[str]
    title: Optional[str]
    description: Optional[str]
    button: Optional[ImageButton] = Field(default_factory=ImageButton)


class ImageWithoutButton(BaseModel):
    image_id: Optional[str]
    title: Optional[str]

from typing import Optional

from pydantic import BaseModel, Field

from .button import ImageButton


class Header(BaseModel):
    text: str


class Footer(BaseModel):
    text: str
    button: Optional[ImageButton] = Field(default_factory=ImageButton)

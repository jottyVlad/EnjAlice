from typing import Optional, Dict

from pydantic import BaseModel


class BaseButton(BaseModel):
    url: Optional[str]
    payload: Optional[Dict]


class ImageButton(BaseButton):
    text: Optional[str]


class ResponseButton(BaseButton):
    title: str
    hide: Optional[bool]

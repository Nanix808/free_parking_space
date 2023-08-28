from pydantic import BaseModel
from typing import Optional, Union


class Offer(BaseModel):
    sdp: str
    type: str
    client_id: Optional[bool | int]
    setting: Optional[str | int]
    rtsp: Union[str, int] = None

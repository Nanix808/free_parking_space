from pydantic import BaseModel
from typing import List

class TunedModel(BaseModel):
    class Config:
        from_attributes = True


class Circle(TunedModel):
    x1: int
    y1:  int
    rad:  float
    x2:  int
    y2:  int


class ParkingCreate(BaseModel):
    rtsp: str
    name: str 
    conf: float
    iou: float
    circle: List[Circle]


class ParkingReady(BaseModel):
    id : int
    rtsp: str
    name: str 
    conf: float
    iou: float
    circle: List[Circle]
   


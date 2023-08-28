
from pydantic import BaseModel, Field, validator
from typing import Optional, Union, List
import uuid
from enum import Enum
from datetime import datetime, datetime


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
   

 # class ResumeCreate(TunedModel):
#     url: str = Field(max_length=128)
#     source: str = Field(max_length=64, default='parsing')
#     content: str = Field()
#     available: Optional[bool]
#     content_limit: Optional[str]
#     content_gpt: Optional[str]
#     age: Optional[int]
#     first_name: Optional[str]
#     last_name: Optional[str]
#     gender: Optional[Gender]
#     education: Optional[Education]
#     experience: Optional[str]
#     skills: Optional[str]
#     profession: Optional[str]
#     languages: Optional[str]
#     courses: Optional[str]
#     computer_skills: Optional[str]

#     class Config:
#         use_enum_values = True


# class ShowResume(TunedModel):
#     id:  int
#     url: str
#     source: str
#     content: str
#     available: bool
#     created_on: Optional[datetime]
#     content_limit: Optional[str]
#     content_gpt: Optional[str]
#     age: Optional[int]
#     first_name: Optional[str]
#     last_name: Optional[str]
#     gender: Optional[str]
#     education: Optional[str]
#     experience: Optional[str]
#     skills: Optional[str]
#     profession: Optional[str]
#     languages: Optional[str]
#     courses: Optional[str]
#     computer_skills: Optional[str]

#     # @validator('content')
#     # def name_must_contain_space(cls, v):
#     #     return v[:100]


# class CreateShowResume(TunedModel):
#     id: int
#     url: str
#     source: str
#     content: str
#     # created_on: Optional[datetime]
#     available: bool
#     content_limit: Optional[str]
#     content_gpt: Optional[str]
#     age: Optional[int]
#     first_name: Optional[str]
#     last_name: Optional[str]
#     gender: Optional[str]
#     education: Optional[str]
#     experience: Optional[str]
#     skills: Optional[str]
#     profession: Optional[str]
#     languages: Optional[str]
#     courses: Optional[str]
#     computer_skills: Optional[str]

#     @validator('content')
#     def name_must_contain_space(cls, v):
#         return v[:100]


# class Resume_Get_Id(TunedModel):
#     id: Optional[int]


# class UpdateResume(TunedModel):
#     name: Optional[str]
#     url: Optional[str]
#     source: Optional[str]
#     content: Optional[str]

from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text, JSON, Text
from sqlalchemy.dialects.mysql import INTEGER
from api.database import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from typing import Optional
import enum
import sqlalchemy


# class Resume(Base):
#     __tablename__ = 'resume'
#     # Обязательные поля______________________________________________

#     # поле id генерируется автоматически его не надо передавать
#     id = mapped_column(Integer, primary_key=True, autoincrement=True)
#     url = mapped_column(String(128), nullable=False)
#     # поле в которое можно передавать значение "parsing", "pdf", "word"
#     source = mapped_column(sqlalchemy.Enum(
#         "parsing", "pdf", "word", name="source_enum"))
#     # поле со всем текстом резюме
#     content = mapped_column(Text, nullable=False)
#     created_on = Column(TIMESTAMP, nullable=False,
#                         server_default=text("CURRENT_TIMESTAMP"))
#     # поле в которое не обязательно передавать значение по умолчанию поставит TRUE
#     available = Column(Boolean, nullable=False, default=True)

#     # Необязательные поля______________________________________________
#     content = mapped_column(Text, nullable=False)
#     content_limit = mapped_column(Text, nullable=True)
#     content_gpt = mapped_column(Text, nullable=True)
#     age: Mapped[Optional[int]] = mapped_column(nullable=True)
#     first_name: Mapped[Optional[str]] = mapped_column(
#         String(128), nullable=True)
#     last_name: Mapped[Optional[str]] = mapped_column(
#         String(128), nullable=True)
#     # поле в которое можно передавать значение "m", "f"
#     gender: Mapped[Optional[str]] = mapped_column(
#         sqlalchemy.Enum("m", "f", name="gender_enum"))
#     # поле в которое можно передавать значение "hight", "low"
#     education: Mapped[Optional[str]] = mapped_column(
#         sqlalchemy.Enum("high", "low", name="education_enum"), nullable=True)
#     experience: Mapped[Optional[str]] = mapped_column(
#         String(128), nullable=True)
#     skills: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
#     profession: Mapped[Optional[str]] = mapped_column(
#         String(128), nullable=True)
#     languages: Mapped[Optional[str]] = mapped_column(
#         String(256), nullable=True)
#     courses: Mapped[Optional[str]] = mapped_column(String(256), nullable=True)
#     computer_skills: Mapped[Optional[str]] = mapped_column(
#         String(256), nullable=True)


class Parking(Base):
  __tablename__ = 'parking'

  id = mapped_column(Integer, primary_key=True, autoincrement=True)
  rtsp = mapped_column(String(256), nullable=False, unique=True)
  available = Column(Boolean, nullable=False, default=True)
  name = mapped_column(String(128), nullable=False)
  conf = Column(Integer, nullable=False, default=0.3)
  iou = Column(Integer, nullable=False, default=0.7)
  circle = mapped_column(JSON, nullable=False)

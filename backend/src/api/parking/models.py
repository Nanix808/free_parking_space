from sqlalchemy import Column, Integer, String, Boolean, JSON
from api.database import Base
from sqlalchemy.orm import mapped_column



class Parking(Base):
  __tablename__ = 'parking'

  id = mapped_column(Integer, primary_key=True, autoincrement=True)
  rtsp = mapped_column(String(256), nullable=False, unique=True)
  available = Column(Boolean, nullable=False, default=True)
  name = mapped_column(String(128), nullable=False)
  conf = Column(Integer, nullable=False, default=0.3)
  iou = Column(Integer, nullable=False, default=0.7)
  circle = mapped_column(JSON, nullable=False)

from sqlalchemy import Column, Integer, String, Text
from .base import Base

class Instinct(Base):
    __tablename__ = "instinct"

    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True, nullable=False)  # sp, so, sx
    label = Column(Text)
    description = Column(Text)

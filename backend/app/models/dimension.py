from sqlalchemy import Column, Integer, String, Text
from app.db import Base

class Dimension(Base):
    __tablename__ = "dimension"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, nullable=False)   # ex: "Type1"
    label = Column(Text, nullable=True)
    center = Column(String, nullable=True)
    integration_target = Column(String, nullable=True)
    disintegration_target = Column(String, nullable=True)
    description = Column(Text, nullable=True)

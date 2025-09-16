from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.db import Base

class Facet(Base):
    __tablename__ = "facet"

    id = Column(Integer, primary_key=True, index=True)
    dimension_id = Column(Integer, ForeignKey("dimension.id"))
    code = Column(String, nullable=True)
    label = Column(Text, nullable=True)
    description = Column(Text, nullable=True)

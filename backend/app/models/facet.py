from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Facet(Base):
    __tablename__ = "facet"

    id = Column(Integer, primary_key=True)
    dimension_id = Column(Integer, ForeignKey("dimension.id"), nullable=False)
    code = Column(String)
    label = Column(Text)
    description = Column(Text)

    dimension = relationship("Dimension", back_populates="facets")

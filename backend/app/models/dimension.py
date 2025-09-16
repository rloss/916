from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Dimension(Base):
    __tablename__ = "dimension"

    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True, nullable=False)
    label = Column(Text)
    center = Column(String, nullable=False)  # gut | heart | head
    integration_target = Column(String, ForeignKey("dimension.code"))
    disintegration_target = Column(String, ForeignKey("dimension.code"))
    description = Column(Text)

    facets = relationship("Facet", back_populates="dimension")

from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey
from app.models.base import Base

class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    test_version_id = Column(Integer, ForeignKey("test_version.id"), nullable=False)
    stem = Column(Text, nullable=False)
    reverse_scored = Column(Boolean, nullable=False, default=False)
    response_scale = Column(Text, nullable=False, default="LIKERT_5")
    locale = Column(Text)
    dimension_code = Column(Text, ForeignKey("dimension.code"))
    facet_id = Column(Integer, ForeignKey("facet.id"))
    instinct_code = Column(Text, ForeignKey("instinct.code"))
    wing_target = Column(Text, ForeignKey("dimension.code"))
    health_level = Column(Integer)
    validity_tag = Column(Text)
    is_active = Column(Boolean, nullable=False, default=True)

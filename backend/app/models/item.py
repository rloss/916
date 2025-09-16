from sqlalchemy import Column, Integer, Text, Boolean, String, ForeignKey
from app.db import Base

class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True)
    test_version_id = Column(Integer, ForeignKey("test_version.id"), nullable=False)
    stem = Column(Text, nullable=False)
    reverse_scored = Column(Boolean, nullable=False, server_default="false")
    response_scale = Column(String, nullable=False, server_default="LIKERT_5")
    dimension_id = Column(Integer, ForeignKey("dimension.id"), nullable=True)
    facet_id = Column(Integer, ForeignKey("facet.id"), nullable=True)
    locale = Column(String, nullable=True)  # e.g., 'ko', 'en'
    is_active = Column(Boolean, nullable=False, server_default="true")

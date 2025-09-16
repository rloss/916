from sqlalchemy import Column, Integer, Text, Boolean, String, ForeignKey
from app.db import Base

class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True)
    test_version_id = Column(Integer, ForeignKey("test_version.id"))
    stem = Column(Text, nullable=False)     # 질문 텍스트
    reverse_scored = Column(Boolean, default=False)
    response_scale = Column(String, nullable=True)   # Likert scale 정의
    dimension_id = Column(Integer, ForeignKey("dimension.id"), nullable=True)
    facet_id = Column(Integer, ForeignKey("facet.id"), nullable=True)
    is_active = Column(Boolean, default=True)

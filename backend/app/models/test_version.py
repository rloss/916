from sqlalchemy import Column, Integer, Text, JSON, TIMESTAMP
from sqlalchemy.sql import func
from app.models.base import Base

class TestVersion(Base):
    __tablename__ = "test_version"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    status = Column(Text, nullable=False, default="draft")
    scoring_model = Column(Text, nullable=False, default="WS_v1")
    locales_supported = Column(JSON)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

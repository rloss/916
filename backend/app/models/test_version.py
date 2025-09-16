from sqlalchemy import Column, Integer, Text, String, TIMESTAMP
from sqlalchemy.sql import func
from app.db import Base

class TestVersion(Base):
    __tablename__ = "test_version"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    status = Column(String, nullable=True)
    scoring_model = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

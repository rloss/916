from sqlalchemy import Column, Integer, Text, String, TIMESTAMP, CheckConstraint
from sqlalchemy.sql import func
from app.db import Base

class TestVersion(Base):
    __tablename__ = "test_version"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    status = Column(String, nullable=False, server_default="draft")
    scoring_model = Column(String, nullable=False, server_default="WS_v1")
    locales_supported = Column(String, nullable=True)  # keep JSON string if you prefer; or switch to JSONB
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    __table_args__ = (
        CheckConstraint("status IN ('draft','active','deprecated')", name="ck_test_version_status"),
    )

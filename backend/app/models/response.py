from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.db import Base

class Response(Base):
    __tablename__ = "response"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(UUID(as_uuid=True), ForeignKey("session.id", ondelete="CASCADE"))
    item_id = Column(Integer, ForeignKey("item.id"))
    raw_choice = Column(Integer, nullable=False)   # 1~5
    scored_value = Column(Integer, nullable=True)  # 0~1 scaled (×100 if int), or swap to NUMERIC if needed
    response_ms = Column(Integer, nullable=True)
    shown_at = Column(TIMESTAMP(timezone=True), nullable=True)
    submitted_at = Column(TIMESTAMP(timezone=True), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

from sqlalchemy import Column, Integer, Text, ForeignKey, TIMESTAMP, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.models.base import Base

class Response(Base):
    __tablename__ = "response"

    id = Column(Integer, primary_key=True)
    session_id = Column(UUID(as_uuid=True), ForeignKey("session.id", ondelete="CASCADE"))
    item_id = Column(Integer, ForeignKey("item.id"))
    raw_choice = Column(Integer, nullable=False)
    scored_value = Column(Numeric)
    response_ms = Column(Integer)
    shown_at = Column(TIMESTAMP(timezone=True))
    submitted_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

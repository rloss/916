from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.db import Base

class Response(Base):
    __tablename__ = "response"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(UUID(as_uuid=True), ForeignKey("session.id"))
    item_id = Column(Integer, ForeignKey("item.id"))
    raw_choice = Column(Integer, nullable=False)   # 선택한 값
    scored_value = Column(Integer, nullable=True)  # 점수로 변환된 값
    response_ms = Column(Integer, nullable=True)   # 응답 시간
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

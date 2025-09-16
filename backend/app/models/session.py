from sqlalchemy import Column, Text, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
import uuid

from app.models.base import Base

class Session(Base):
    __tablename__ = "session"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(Text)
    form_id = Column(Integer, ForeignKey("form.id"))
    started_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    completed_at = Column(TIMESTAMP(timezone=True))
    locale = Column(Text)
    device_meta = Column(JSONB)

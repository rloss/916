from sqlalchemy import Column, Integer, String, JSON, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.db import Base

class ScoreProfile(Base):
    __tablename__ = "score_profile"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(UUID(as_uuid=True), ForeignKey("session.id"), unique=True)
    model_used = Column(String, nullable=True)
    raw_sum = Column(JSON, nullable=True)
    normalized = Column(JSON, nullable=True)
    main_type = Column(String, nullable=True)
    wing_distribution = Column(JSON, nullable=True)
    health = Column(JSON, nullable=True)
    integration = Column(JSON, nullable=True)
    disintegration = Column(JSON, nullable=True)
    center_scores = Column(JSON, nullable=True)
    subtypes = Column(JSON, nullable=True)
    validity = Column(JSON, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

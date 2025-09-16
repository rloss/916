from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from app.db import Base

class ScoreProfile(Base):
    __tablename__ = "score_profile"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(UUID(as_uuid=True), ForeignKey("session.id", ondelete="CASCADE"), unique=True)
    model_used = Column(String, nullable=True)
    theta = Column(JSONB, nullable=True)
    theta_se = Column(JSONB, nullable=True)
    raw_sum = Column(JSONB, nullable=True)
    normalized = Column(JSONB, nullable=True)
    main_type = Column(String, ForeignKey("dimension.code"), nullable=True)
    wing_distribution = Column(JSONB, nullable=True)
    health = Column(JSONB, nullable=True)
    integration = Column(JSONB, nullable=True)
    disintegration = Column(JSONB, nullable=True)
    center_scores = Column(JSONB, nullable=True)
    subtypes = Column(JSONB, nullable=True)
    validity = Column(JSONB, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

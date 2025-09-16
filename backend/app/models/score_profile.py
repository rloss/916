from sqlalchemy import Column, Integer, Text, ForeignKey, TIMESTAMP, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.models.base import Base

class ScoreProfile(Base):
    __tablename__ = "score_profile"

    id = Column(Integer, primary_key=True)
    session_id = Column(UUID(as_uuid=True), ForeignKey("session.id", ondelete="CASCADE"), unique=True)
    model_used = Column(Text)
    theta = Column(JSON)
    theta_se = Column(JSON)
    raw_sum = Column(JSON)
    normalized = Column(JSON)
    main_type = Column(Text, ForeignKey("dimension.code"))
    wing_distribution = Column(JSON)
    health = Column(JSON)
    integration = Column(JSON)
    disintegration = Column(JSON)
    center_scores = Column(JSON)
    subtypes = Column(JSON)
    validity = Column(JSON)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

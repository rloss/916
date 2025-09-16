from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, CheckConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from app.db import Base

class ItemParam(Base):
    __tablename__ = "item_param"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("item.id"), nullable=False)
    model = Column(String, nullable=False)  # WS | 2PL | MIRT
    weight = Column(JSONB, nullable=True)   # WS weights {E1:1.0,...}
    a = Column(JSONB, nullable=True)        # IRT discrimination (vector/matrix)
    b = Column(JSONB, nullable=True)        # IRT difficulty (thresholds)
    c = Column(Integer, nullable=True)      # 3PL guessing
    last_calibrated_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    __table_args__ = (
        CheckConstraint("model IN ('WS','2PL','MIRT')", name="ck_item_param_model"),
    )

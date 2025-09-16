from sqlalchemy import Column, Integer, Text, ForeignKey, JSON, TIMESTAMP, Numeric
from sqlalchemy.sql import func
from app.models.base import Base

class ItemParam(Base):
    __tablename__ = "item_param"

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey("item.id", ondelete="CASCADE"), nullable=False)
    model = Column(Text, nullable=False)
    weight = Column(JSON)
    a = Column(JSON)
    b = Column(JSON)
    c = Column(Numeric)
    last_calibrated_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

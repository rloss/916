from sqlalchemy import Column, Integer, String, JSON, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from app.db import Base

class ItemParam(Base):
    __tablename__ = "item_param"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("item.id"))
    model = Column(String, nullable=True)
    weight = Column(JSON, nullable=True)
    a = Column(JSON, nullable=True)
    b = Column(JSON, nullable=True)
    c = Column(Integer, nullable=True)
    last_calibrated_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

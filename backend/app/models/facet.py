from sqlalchemy import Column, Integer, String, Text, ForeignKey, CheckConstraint
from app.db import Base

class Facet(Base):
    __tablename__ = "facet"

    id = Column(Integer, primary_key=True, index=True)
    dimension_id = Column(Integer, ForeignKey("dimension.id"), nullable=False)
    code = Column(String)  # sp | so | sx
    label = Column(Text)
    description = Column(Text)

    __table_args__ = (
        CheckConstraint("code IN ('sp','so','sx')", name="ck_facet_code"),
    )

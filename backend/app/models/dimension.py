from sqlalchemy import Column, Integer, String, Text, CheckConstraint, ForeignKey
from app.db import Base

class Dimension(Base):
    __tablename__ = "dimension"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, nullable=False, unique=True)  # E1..E9
    label = Column(Text)
    center = Column(String)  # gut | heart | head
    # self-reference by code
    integration_target = Column(String, ForeignKey("dimension.code"), nullable=True)
    disintegration_target = Column(String, ForeignKey("dimension.code"), nullable=True)
    description = Column(Text)

    __table_args__ = (
        CheckConstraint("center IN ('gut','heart','head')", name="ck_dimension_center"),
        CheckConstraint("code ~ '^E[1-9]$'", name="ck_dimension_code_format"),
    )

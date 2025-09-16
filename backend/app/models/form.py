from sqlalchemy import Column, Integer, Text, String, ForeignKey, CheckConstraint
from sqlalchemy.dialects.postgresql import JSONB
from app.db import Base

class Form(Base):
    __tablename__ = "form"

    id = Column(Integer, primary_key=True, index=True)
    test_version_id = Column(Integer, ForeignKey("test_version.id"), nullable=True)
    name = Column(Text, nullable=True)
    mode = Column(String, nullable=False, server_default="fixed")  # fixed | adaptive
    item_ids = Column(JSONB, nullable=True)     # [1,2,3,...] for fixed mode
    length_target = Column(Integer, nullable=True)
    time_limit_sec = Column(Integer, nullable=True)

    __table_args__ = (
        CheckConstraint("mode IN ('fixed','adaptive')", name="ck_form_mode"),
    )

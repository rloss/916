from sqlalchemy import Column, Integer, Text, ForeignKey, JSON
from app.models.base import Base

class Form(Base):
    __tablename__ = "form"

    id = Column(Integer, primary_key=True)
    test_version_id = Column(Integer, ForeignKey("test_version.id"))
    name = Column(Text)
    mode = Column(Text, nullable=False, default="fixed")  # fixed | adaptive
    item_ids = Column(JSON)
    length_target = Column(Integer)
    time_limit_sec = Column(Integer)

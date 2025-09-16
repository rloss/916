from sqlalchemy import Column, Integer, Text, ForeignKey, JSON
from app.models.base import Base

class Norms(Base):
    __tablename__ = "norms"

    id = Column(Integer, primary_key=True)
    test_version_id = Column(Integer, ForeignKey("test_version.id"))
    locale = Column(Text)
    cohort_filters = Column(JSON)
    method = Column(Text, nullable=False, default="empirical")
    percentiles = Column(JSON)

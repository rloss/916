from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint
from sqlalchemy.dialects.postgresql import JSONB
from app.db import Base

class Norms(Base):
    __tablename__ = "norms"

    id = Column(Integer, primary_key=True, index=True)
    test_version_id = Column(Integer, ForeignKey("test_version.id"))
    locale = Column(String, nullable=True)
    cohort_filters = Column(JSONB, nullable=True)  # {"age":"20-29","gender":"F"}
    method = Column(String, nullable=False, server_default="empirical")  # empirical | gaussian
    percentiles = Column(JSONB, nullable=True)

    __table_args__ = (
        CheckConstraint("method IN ('empirical','gaussian')", name="ck_norms_method"),
    )

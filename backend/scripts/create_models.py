import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "app", "models")

files = {
    "test_version.py": """from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.sql import func
from app.db import Base

class TestVersion(Base):
    __tablename__ = "test_version"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    status = Column(String, default="draft")  # draft, active, deprecated
    scoring_model = Column(String, default="WS_v1")
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
""",
    "dimension.py": """from sqlalchemy import Column, Integer, String, Text
from app.db import Base

class Dimension(Base):
    __tablename__ = "dimension"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, nullable=False)  # E1..E9
    label = Column(Text)
    center = Column(String)  # gut, heart, head
    integration_target = Column(String)
    disintegration_target = Column(String)
    description = Column(Text)
""",
    "facet.py": """from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.db import Base

class Facet(Base):
    __tablename__ = "facet"

    id = Column(Integer, primary_key=True, index=True)
    dimension_id = Column(Integer, ForeignKey("dimension.id"))
    code = Column(String)  # sp, so, sx
    label = Column(Text)
    description = Column(Text)
""",
    "item.py": """from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from app.db import Base

class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True)
    test_version_id = Column(Integer, ForeignKey("test_version.id"))
    stem = Column(Text, nullable=False)
    reverse_scored = Column(Boolean, default=False)
    response_scale = Column(String, default="LIKERT_5")
    dimension = Column(String)  # E1..E9
    facet = Column(String)      # sp/so/sx
    is_active = Column(Boolean, default=True)
""",
    "item_param.py": """from sqlalchemy import Column, Integer, String, JSON, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from app.db import Base

class ItemParam(Base):
    __tablename__ = "item_param"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("item.id"))
    model = Column(String)  # WS | IRT | MIRT
    weight = Column(JSON)
    a = Column(JSON)        # IRT 변별도
    b = Column(JSON)        # IRT 난이도
    c = Column(Integer)     # IRT 추측도
    last_calibrated_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
""",
    "session.py": """from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql import func
from app.db import Base

class Session(Base):
    __tablename__ = "session"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(String, nullable=True)
    form_id = Column(String, nullable=True)
    started_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    completed_at = Column(TIMESTAMP(timezone=True), nullable=True)
""",
    "response.py": """from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from app.db import Base

class Response(Base):
    __tablename__ = "response"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(UUID(as_uuid=True), ForeignKey("session.id"))
    item_id = Column(Integer, ForeignKey("item.id"))
    raw_choice = Column(Integer, nullable=False)
    scored_value = Column(Integer, nullable=True)
    response_ms = Column(Integer, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
""",
    "score_profile.py": """from sqlalchemy import Column, Integer, String, JSON, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from app.db import Base

class ScoreProfile(Base):
    __tablename__ = "score_profile"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, ForeignKey("session.id"), unique=True)
    model_used = Column(String)
    raw_sum = Column(JSON)
    normalized = Column(JSON)
    main_type = Column(String)
    wing_distribution = Column(JSON)
    health = Column(JSON)
    integration = Column(JSON)
    disintegration = Column(JSON)
    center_scores = Column(JSON)
    subtypes = Column(JSON)
    validity = Column(JSON)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
""",
    "__init__.py": """from app.db import Base
from app.models.test_version import TestVersion
from app.models.dimension import Dimension
from app.models.facet import Facet
from app.models.item import Item
from app.models.item_param import ItemParam
from app.models.session import Session
from app.models.response import Response
from app.models.score_profile import ScoreProfile

__all__ = [
    "Base",
    "TestVersion",
    "Dimension",
    "Facet",
    "Item",
    "ItemParam",
    "Session",
    "Response",
    "ScoreProfile",
]
"""
}

def main():
    os.makedirs(MODELS_DIR, exist_ok=True)
    for filename, content in files.items():
        path = os.path.join(MODELS_DIR, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"✅ Created {path}")

if __name__ == "__main__":
    main()

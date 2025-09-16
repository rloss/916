import os

BASE_DIR = "backend"

# 디렉토리 구조 정의
dirs = [
    f"{BASE_DIR}/app",
    f"{BASE_DIR}/app/models",
    f"{BASE_DIR}/app/routers",
    f"{BASE_DIR}/app/schemas",
    f"{BASE_DIR}/app/services",
    f"{BASE_DIR}/tests",
]

# 파일 템플릿
files = {
    f"{BASE_DIR}/app/__init__.py": "",
    f"{BASE_DIR}/app/main.py": """from fastapi import FastAPI
from app.routers import items, scoring

app = FastAPI(title="Enneagram Test API")

app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(scoring.router, prefix="/score", tags=["score"])

@app.get("/")
def root():
    return {"message": "Enneagram Test API is running"}
""",
    f"{BASE_DIR}/app/db.py": """from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/enneagram")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
""",
    f"{BASE_DIR}/app/models/__init__.py": "",
    f"{BASE_DIR}/app/models/item.py": """from sqlalchemy import Column, Integer, String, Boolean
from app.db import Base

class Item(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True, index=True)
    stem = Column(String, nullable=False)
    reverse_scored = Column(Boolean, default=False)
    response_scale = Column(String, default="LIKERT_5")
    dimension = Column(String, nullable=True)   # E1..E9
    facet = Column(String, nullable=True)       # sp/so/sx
""",
    f"{BASE_DIR}/app/routers/__init__.py": "",
    f"{BASE_DIR}/app/routers/items.py": """from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_items():
    return {"items": "List of items will go here"}
""",
    f"{BASE_DIR}/app/routers/scoring.py": """from fastapi import APIRouter
from app.schemas.score import Response, ScoreResult
from app.services.scoring import score_session

router = APIRouter()

@router.post("/", response_model=ScoreResult)
def calculate_score(responses: list[Response]):
    # TODO: 실제 DB 연결해서 items 가져오기
    items = {
        1: {"reverse_scored": False, "response_scale": "LIKERT_5", "dimension": "E1", "facet": None},
        2: {"reverse_scored": True, "response_scale": "LIKERT_5", "dimension": "E1", "facet": None}
    }
    item_params = {
        1: {"weight": {"E1": 1.0}},
        2: {"weight": {"E1": 1.0}}
    }
    main_dimensions = ["E1","E2","E3","E4","E5","E6","E7","E8","E9"]
    subtype_facets = ["sp","so","sx"]

    result = score_session([r.dict() for r in responses], items, item_params, main_dimensions, subtype_facets)
    return result
""",
    f"{BASE_DIR}/app/schemas/__init__.py": "",
    f"{BASE_DIR}/app/schemas/score.py": """from pydantic import BaseModel
from typing import Dict

class Response(BaseModel):
    item_id: int
    raw_choice: int

class ScoreResult(BaseModel):
    main_type: str
    normalized: Dict[str, float]
    wing_distribution: Dict[str, float]
    center_scores: Dict[str, float]
    subtypes: Dict[str, float]
    validity: Dict[str, float]
""",
    f"{BASE_DIR}/app/services/__init__.py": "",
    f"{BASE_DIR}/app/services/scoring.py": """import math
from collections import defaultdict

def sigmoid(x): return 1 / (1 + math.exp(-x))

def softmax(values: dict):
    exp_values = {k: math.exp(v) for k, v in values.items()}
    total = sum(exp_values.values())
    return {k: v / total for k, v in exp_values.items()}

def score_session(responses, items, item_params, main_dimensions, subtype_facets):
    scored = {}
    for r in responses:
        item = items[r["item_id"]]
        scale = item.get("response_scale", "LIKERT_5")
        max_val = int(scale.split("_")[1])
        x = (r["raw_choice"] - 1) / (max_val - 1)
        if item["reverse_scored"]:
            x = 1 - x
        scored[r["item_id"]] = x

    raw_sum = defaultdict(float)
    for item_id, x in scored.items():
        weights = item_params[item_id].get("weight", {})
        for d, w in weights.items():
            raw_sum[d] += w * x

    min_score = min(raw_sum.values()) if raw_sum else 0
    max_score = max(raw_sum.values()) if raw_sum else 1
    normalized = {d: 100 * (s - min_score) / (max_score - min_score + 1e-6) for d, s in raw_sum.items()}

    main_type = max(normalized, key=normalized.get)
    idx = main_dimensions.index(main_type)
    neighbors = [main_dimensions[(idx - 1) % len(main_dimensions)], main_dimensions[(idx + 1) % len(main_dimensions)]]
    wing_distribution = softmax({n: normalized[n] for n in neighbors})

    centers = {
        "gut": (normalized.get("E8",0)+normalized.get("E9",0)+normalized.get("E1",0))/3,
        "heart": (normalized.get("E2",0)+normalized.get("E3",0)+normalized.get("E4",0))/3,
        "head": (normalized.get("E5",0)+normalized.get("E6",0)+normalized.get("E7",0))/3,
    }

    subtypes = {f: 0 for f in subtype_facets}
    validity = {"infrequency": 0, "inconsistency": 0, "acquiescence": sum(scored.values())/len(scored) if scored else 0}

    return {
        "main_type": main_type,
        "normalized": normalized,
        "wing_distribution": wing_distribution,
        "center_scores": centers,
        "subtypes": subtypes,
        "validity": validity
    }
""",
    f"{BASE_DIR}/tests/test_scoring.py": """from app.services.scoring import score_session

def test_scoring_basic():
    responses = [{"item_id":1,"raw_choice":5},{"item_id":2,"raw_choice":1}]
    items = {
        1: {"reverse_scored": False, "response_scale": "LIKERT_5", "dimension": "E1", "facet": None},
        2: {"reverse_scored": True, "response_scale": "LIKERT_5", "dimension": "E1", "facet": None}
    }
    item_params = {1: {"weight":{"E1":1.0}}, 2: {"weight":{"E1":1.0}}}
    main_dimensions = ["E1","E2","E3","E4","E5","E6","E7","E8","E9"]
    subtype_facets = ["sp","so","sx"]
    result = score_session(responses, items, item_params, main_dimensions, subtype_facets)
    assert "main_type" in result
"""
}

def create_structure():
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        print(f"Created directory: {d}")

    for path, content in files.items():
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Created file: {path}")

if __name__ == "__main__":
    create_structure()
    print("✅ Backend skeleton created!")

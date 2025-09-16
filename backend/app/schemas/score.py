from pydantic import BaseModel
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

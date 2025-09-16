from fastapi import APIRouter
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

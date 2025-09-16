from app.services.scoring import score_session

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

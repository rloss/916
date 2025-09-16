import math
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

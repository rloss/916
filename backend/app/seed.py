from sqlalchemy.orm import Session
from app.db import engine
from app.models import TestVersion, Dimension, Facet, Instinct

def seed():
    with Session(engine) as session:
        # 1. TestVersion 기본값
        tv = TestVersion(
            name="Enneagram v1",
            status="active",
            scoring_model="WS_v1",
            locales_supported="en,ko"
        )
        session.add(tv)

        # 2. Dimension (9유형)
        dimensions = [
            {"code": "E1", "label": "The Reformer", "center": "gut",
             "integration_target": "E7", "disintegration_target": "E4"},
            {"code": "E2", "label": "The Helper", "center": "heart",
             "integration_target": "E4", "disintegration_target": "E8"},
            {"code": "E3", "label": "The Achiever", "center": "heart",
             "integration_target": "E6", "disintegration_target": "E9"},
            {"code": "E4", "label": "The Individualist", "center": "heart",
             "integration_target": "E1", "disintegration_target": "E2"},
            {"code": "E5", "label": "The Investigator", "center": "head",
             "integration_target": "E8", "disintegration_target": "E7"},
            {"code": "E6", "label": "The Loyalist", "center": "head",
             "integration_target": "E9", "disintegration_target": "E3"},
            {"code": "E7", "label": "The Enthusiast", "center": "head",
             "integration_target": "E5", "disintegration_target": "E1"},
            {"code": "E8", "label": "The Challenger", "center": "gut",
             "integration_target": "E2", "disintegration_target": "E5"},
            {"code": "E9", "label": "The Peacemaker", "center": "gut",
             "integration_target": "E3", "disintegration_target": "E6"},
        ]
        session.add_all([Dimension(**d) for d in dimensions])

        # 3. Facet (예시 몇 개, 확장 가능)
        facets = [
            {"dimension_id": 1, "code": "perfectionistic", "label": "Perfectionistic"},
            {"dimension_id": 2, "code": "caring", "label": "Caring"},
            {"dimension_id": 3, "code": "driven", "label": "Driven"},
        ]
        session.add_all([Facet(**f) for f in facets])

        # 4. Instinct (sp/so/sx)
        instincts = [
            {"code": "sp", "label": "Self-preservation", "description": "Focus on safety, comfort, and resources."},
            {"code": "so", "label": "Social", "description": "Focus on relationships, belonging, and status."},
            {"code": "sx", "label": "Sexual/One-to-One", "description": "Focus on intensity, bonding, and passion."},
        ]
        session.add_all([Instinct(**i) for i in instincts])

        # Commit
        session.commit()
        print("✅ Seed data inserted.")

if __name__ == "__main__":
    seed()

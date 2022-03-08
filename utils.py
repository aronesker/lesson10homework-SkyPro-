import json

def load_candidates():
    with open("candidates.json", "r", encoding="utf-8") as file:
        candidates = json.load(file)

    return candidates

def get_candidate_by_id(uid):
    candidates = load_candidates()
    for candidate in candidates:
        if candidate["id"] == uid:
            return candidate

def get_candidates_by_skill(skill):
    candidates = load_candidates()
    skill_lower = skill.lower()
    skilled_candidates = []
    for candidate in candidates:
        candidate_skills = candidate["skills"].lower().split(", ")
        if skill_lower in candidate_skills:
            skilled_candidates.append(candidate)

    return skilled_candidates
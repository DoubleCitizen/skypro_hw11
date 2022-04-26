import json


def load_candidates_from_json(path):
    """возвращает список всех кандидатов"""
    with open(path, "r", encoding="UTF-8") as file:
        candidates_list = json.load(file)

    return candidates_list


def get_candidate(candidates_list, candidate_id):
    """возвращает одного кандидата по его id"""
    for candidate in candidates_list:
        if candidate['id'] == candidate_id:
            return candidate
    return None


def get_candidates_by_name(candidates_list, candidate_name):
    """возвращает кандидатов по имени"""
    conformity = []
    for candidate in candidates_list:
        if candidate_name.lower() in candidate['name'].lower():
            conformity.append(candidate)
    return conformity


def get_candidates_by_skill(candidates_list, skill_name):
    """возвращает кандидатов по навыку"""
    conformity = []
    for candidate in candidates_list:
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            conformity.append(candidate)
    return conformity

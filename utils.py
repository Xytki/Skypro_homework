import json

from candidate import Candidate


def load_candidates():
    """загрузит данные из файла"""
    with open('candidates.json', 'r', encoding='utf-8') as f:
        templates = json.load(f)
    return templates


def get_all(templates):
    """покажет всех кандидатов"""
    spis = []
    for i in templates:
        candidate = Candidate(i['pk'], i['name'], i['position'], i['skills'].lower(), i['picture'])
        spis.append(candidate)
    return spis


def get_by_pk(pk, data):
    """вернет кандидата по pk"""
    for i in data:
        if i.pk == pk:
            return i


def get_by_skill(skill_name, data):
    """вернет кандидатов по навыку"""
    spis = []
    for i in data:
        if skill_name in i.skills:
            spis.append(i)
    return spis

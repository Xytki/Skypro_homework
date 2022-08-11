class Candidate:
    """Класс который выводит необходимую информацию о кондидатах"""
    def __init__(self, pk, name, position, skills, picture):
        self.pk = pk
        self.name = name
        self.position = position
        self.skills = skills
        self.picture = picture

    def __repr__(self):
        return f'Имя кандидата - {self.name}\n' \
               f'Позиция кандидата - {self.position}\n' \
               f'Навыки - {self.skills}'

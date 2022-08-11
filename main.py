from flask import Flask

from utils import get_all, load_candidates, get_by_pk, get_by_skill

app = Flask(__name__)

data = get_all(load_candidates())


@app.route("/")
def page_index():
    """главная страница - выводит информацию о всех кандидатах"""
    str = '<pre>'
    for i in data:
        str += f'{i} \n \n'
    str += '</pre>'
    return str


@app.route('/candidates/<int:pk>')
def get_profile(pk):
    """"""
    user = get_by_pk(pk, data)
    if user:
        sis = f'<img src="{user.picture}">'
        sis += f'<pre>{user} </pre>'
    else:
        sis = "No user"
    return sis


@app.route('/skills/<x>')
def get_skills(x):
    users = get_by_skill(x, data)
    if users:
        sis = '<pre>'
        for i in users:
            sis += f'{i} \n \n'
        sis += '</pre>'
    else:
        sis = 'No skills'

    return sis


app.run()

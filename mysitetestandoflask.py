from flask import Flask
import random

app = Flask(__name__)

facts_list = [
    "Elon Musk afirma que as redes sociais são projetadas para nos manter dentro da plataforma, para que passemos o máximo de tempo possível visualizando conteúdo.",
    "De acordo com um estudo realizado em 2018, mais de 50% das pessoas entre 18 e 34 anos se consideram dependentes de seus smartphones.",
    "As redes sociais têm seus pontos positivos e negativos, e devemos estar conscientes de ambos ao utilizá-las.",
    "O estudo da dependência tecnológica é uma das áreas mais relevantes da pesquisa científica moderna."
]


@app.route("/")
def index():
    return f'''
<h1>Olá! Nesta página você encontrará alguns fatos sobre dependências tecnológicas!
<a href="/random_fact">View a random fact!
'''

@app.route("/random_fact")
def facts():
    return f'<p>{random.choice(facts_list)}'

@app.route("/ENDERECO")
def charada():
    return f'''
<h1>Qual é a tecla favorita de um astronauta no computador? Resposta: A barra de espaço!
'''

app.run(debug=True)

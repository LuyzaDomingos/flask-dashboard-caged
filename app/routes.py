from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ranking')
def ranking():
    return "<h1>Página de Ranking de Atividades</h1>"

@app.route("/estatisticas")
def estatisticas():
    return render_template('estatisticabase.html')

@app.route("/regiao")
def regiao():
    return "<h1>Página de Região</h1>"
from app import app
from flask import Flask, render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ranking')
def ranking():
    return "<h1>Página de Ranking de Atividades</h1>"

@app.route("/estatisticas")
def estatisticas():
    return "<h1>Página de Estatísticas</h1>"


@app.route("/regiao")
def regiao():
    return "<h1>Página de Região</h1>"
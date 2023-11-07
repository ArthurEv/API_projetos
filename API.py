from flask import Flask, request, jsonify
from flask_cors import CORS
from operacoes_banco import *

app = Flask(__name__)
CORS(app)

#endpoint para obter 3 cursos disponíveis para página inicial
@app.route("/3cursosDisponiveis", methods=["GET"])
def obter_3CursosDisponiveis():
    cursos = obter3CursosDisponiveis()
    return jsonify(cursos)

#endpoint para obter 3 cursos que o aluno está matriculado para página inicial
@app.route("/3cursosMatriculados/<int:id>", methods=["GET"])
def obter_3CursosMatriculados(id):
    cursos = obter3CursosMatriculados(id)
    return jsonify(cursos)

#endpoint para obter todos os cursos disponíveis
@app.route("/cursosDisponiveis", methods=["GET"])
def obter_CursosDisponiveis():
    cursos = obterCursosDisponiveis()
    return jsonify(cursos)

#endpoint para obter todos os cursos que o aluno está matriculado
@app.route("/cursosMatriculados/<int:id>", methods=["GET"])
def obter_CursosMatriculados(id):
    cursos = obterCursosMatriculados(id)
    return jsonify(cursos)

#endpoint para obter todas as aulas de um curso
@app.route("/aulas/<int:id>", methods=["GET"])
def obter_Aulas(id):
    aulas = obterAulas(id)
    return jsonify(aulas)

#endpoint para obter dados de uma aula
@app.route("/aula/<int:id>/<int:numero>", methods=["GET"])
def obter_DadosAula(id,numero):
    aula = obterDadosAula(id,numero)
    return jsonify(aula)

app.run()
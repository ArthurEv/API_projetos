from flask import Flask, request, jsonify
from flask_cors import CORS
from operacoes_banco import *

app = Flask(__name__)
CORS(app)

#endpoint para obter todos os cursos disponíveis
@app.route("/cursosDisponiveis", methods=["GET"])
def obter_CursosDisponiveis():
    cursos = obterCursosDisponiveis()
    return jsonify(cursos)

app.run()
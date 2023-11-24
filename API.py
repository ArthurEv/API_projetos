from flask import Flask, request, jsonify
from flask_cors import CORS
from operacoes_banco import *

app = Flask(__name__)
CORS(app)

#endpoint para obter aluno
@app.route("/aluno/<int:id>", methods=["GET"])
def obter_aluno(id):
    aluno = obterAluno(id)
    return jsonify(aluno)

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

#endpoint para obter dados de um curso
@app.route("/curso/<int:id>", methods=["GET"])
def obter_curso(id):
    curso = obterCurso(id)
    return jsonify(curso)

#endpoint para obter todas as aulas de um curso
@app.route("/aulas/<int:idcurso>", methods=["GET"])
def obter_Aulas(idcurso):
    aulas = obterAulas(idcurso)
    return jsonify(aulas)

#endpoint para obter dados de uma aula
@app.route("/aula/<int:idaula>", methods=["GET"])
def obter_DadosAula(idaula):
    aula = obterDadosAula(idaula)
    return jsonify(aula)


#endpoint para cadastrar aluno
@app.route("/aluno", methods=["POST"])
def cadastrar_aluno():
    aluno = request.json
    cadastrarAluno(aluno)
    return (jsonify({"mensagem":"Aluno cadastrado com sucesso"}))

#endpoint para criar fórum
@app.route("/forum", methods=["POST"])
def criar_forum():
    forum = request.json
    criarForum(forum)
    return (jsonify({"mensagem":"Fórum criado com sucesso"}))

#endpoint para obter todos os fóruns
@app.route("/forum", methods=["GET"])
def obter_Foruns():
    foruns = obterForuns()
    return jsonify(foruns)

#endpoint para obter um fórum
@app.route("/forum/<int:id>", methods=["GET"])
def obter_Forum(id):
    forum = obterForum(id)
    return jsonify(forum)

#endpoint para obter todas as mensagens de um fórum
@app.route("/mensagens/<int:idforum>", methods=["GET"])
def obter_Mensagens(idforum):
    mensagens = obterMensagens(idforum)
    return jsonify(mensagens)

#endpoint para cadastrar uma mensagem em um fórum
@app.route("/mensagem", methods=["POST"])
def cadastrar_mensagem():
    mensagem = request.json
    cadastrarMensagem(mensagem)
    return (jsonify({"mensagem":"Mensagem cadastrada com sucesso"}))

#endpoint para cadastrar uma matrícula em um curso
@app.route("/matricula", methods=["POST"])
def cadastrar_matricula():
    matricula = request.json
    cadastrarMatricula(matricula)
    return (jsonify({"mensagem":"Matrícula cadastrada com sucesso"}))

#endpoint para ver se aluno já está matriculado em um curso	
@app.route("/matriculado/<int:idcurso>/<int:idaluno>", methods=["GET"])
def esta_matriculado(idcurso,idaluno):
    matricula = matriculado(idcurso,idaluno)
    return jsonify(matricula)

#endpoint para obter próxima aula de um curso
@app.route("/proximaAula/<int:idcurso>/<int:numero>", methods=["GET"])
def obter_proximaAula(idcurso,numero):
    aula = proximaAula(idcurso,numero)
    return jsonify(aula)

#endpoint para atualizar cadastro de um aluno
@app.route("/atualizarAluno/<int:idaluno>", methods=["PUT"])
def atualizar_aluno(idaluno):
    aluno = request.json
    atualizarAluno(aluno,idaluno)
    return (jsonify({"mensagem":"Aluno atualizado com sucesso"}))


### página de administrador ###

#endpoint para adicionar curso
@app.route("/curso", methods=["POST"])
def adicionar_curso():
    curso = request.json
    insereCurso(curso)
    return (jsonify({"mensagem":"Curso adicionado com sucesso"})) 

#endpoint para atualizar curso
@app.route("/curso/<int:id>", methods=["PUT"])
def atualizar_curso(id):
    curso = request.json
    atualizaCurso(curso,id)
    return (jsonify({"mensagem":"Curso atualizado com sucesso"}))

#endpoint para deletar curso
@app.route("/curso/<int:id>", methods=["DELETE"])
def deletar_curso(id):
    deletaCurso(id)
    return (jsonify({"mensagem":"Curso deletado com sucesso"}))

#endpoint para adicionar aula
@app.route("/aula", methods=["POST"])
def adicionar_aula():
    aula = request.json
    insereAula(aula)
    return (jsonify({"mensagem":"Aula adicionado com sucesso"})) 

#endpoint para atualizar curso
@app.route("/aula/<int:id>", methods=["PUT"])
def atualizar_aula(id):
    aula = request.json
    atualizaAula(aula,id)
    return (jsonify({"mensagem":"Aula atualizado com sucesso"}))

#endpoint para deletar curso
@app.route("/aula/<int:id>", methods=["DELETE"])
def deletar_aula(id):
    deletaAula(id)
    return (jsonify({"mensagem":"Aula deletado com sucesso"}))

#endpoint para obter todos os professor
@app.route("/professores", methods=["GET"])
def obter_Professores():
    professores = obterProfessores()
    return jsonify(professores)

app.run()
import mysql.connector

# Conexão com o banco de dados
def obterConexao():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="projetos"
    )
    return conexao

#Obtém informações do aluno
def obterAluno(id):
    conexao = obterConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM aluno WHERE id = %s",(id,))
    cursos = cursor.fetchall()
    conexao.close()
    return cursos

#Obtém 3 cursos disponíveis para página inicial
def obter3CursosDisponiveis():
    conexao = obterConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT* FROM curso LIMIT 3")
    cursos = cursor.fetchall()
    conexao.close()
    return cursos

#Obtém 3 cursos que o aluno está matriculado para página inicial
def obter3CursosMatriculados(idaluno):
    conexao = obterConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT curso.titulo,curso.descricao,curso.id FROM projetos.matricula AS matricula INNER JOIN projetos.curso AS curso ON matricula.idcurso = curso.id WHERE matricula.idaluno = %s LIMIT 3",(idaluno,))
    cursos = cursor.fetchall()
    conexao.close()
    return cursos

#Obtém todos os cursos disponíveis
def obterCursosDisponiveis():
    conexao = obterConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM curso")
    cursos = cursor.fetchall()
    conexao.close()
    return cursos

#Obtém todos os cursos que o aluno está matriculado
def obterCursosMatriculados(idaluno):
    conexao = obterConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT curso.titulo,curso.descricao,curso.id FROM projetos.matricula AS matricula INNER JOIN projetos.curso AS curso ON matricula.idcurso = curso.id WHERE matricula.idaluno = %s",(idaluno,))
    cursos = cursor.fetchall()
    conexao.close()
    return cursos

#Obtém todas as aulas de um curso
def obterAulas(idcurso):
    conexao = obterConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM aula WHERE idcurso = %s",(idcurso,))
    aulas = cursor.fetchall()
    conexao.close()
    return aulas

#Obtém dados de uma aula
def obterDadosAula(idaula):
    conexao = obterConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM aula WHERE id = %s", (idaula,))
    aula = cursor.fetchone()
    conexao.close()
    return aula

#Cadastra aluno
def cadastrarAluno(aluno):
    conexao = obterConexao()
    cursor = conexao.cursor()
    sql = "INSERT INTO aluno (nome,email,senha,nascimento,responsavel,avatar) VALUES (%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, [aluno['nome'], aluno['email'], aluno['senha'], aluno['nascimento'], aluno['responsavel'], aluno['avatar']])
    conexao.commit()
    conexao.close()

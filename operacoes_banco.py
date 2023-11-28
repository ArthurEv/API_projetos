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

#Verificar se existe aluno com o email e senha informados
def verificarAluno(email,senha):
    conexao = obterConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM aluno WHERE email = %s AND senha = %s",(email,senha))
    aluno = cursor.fetchall()
    conexao.close()
    # if aluno is None:
    #     return "Não existe aluno com o email e senha informados"
    return aluno

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
    cursor.execute("SELECT curso.titulo,curso.descricao,curso.id,curso.quantidade_aulas,curso.idade,curso.idprofessor,professor.nome FROM curso INNER JOIN professor ON curso.idprofessor = professor.id ORDER BY curso.titulo")
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

#Obtém informações de um curso
def obterCurso(idcurso):
    conexao = obterConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT curso.titulo, curso.descricao, curso.id, professor.nome, professor.email FROM projetos.curso AS curso INNER JOIN projetos.professor AS professor ON curso.idprofessor = professor.id WHERE curso.id = %s",(idcurso,))
    curso = cursor.fetchall()
    conexao.close()
    return curso

#Obtém todas as aulas de um curso
def obterAulas(idcurso):
    conexao = obterConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM aula WHERE idcurso = %s ORDER BY numero",(idcurso,))
    aulas = cursor.fetchall()
    conexao.close()
    return aulas

#Obtém dados de uma aula
def obterDadosAula(idaula):
    conexao = obterConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT aula.id, aula.titulo, aula.descricao, aula.video, aula.numero, aula.idcurso, curso.quantidade_aulas FROM aula INNER JOIN curso ON aula.idcurso = curso.id WHERE aula.id = %s", (idaula,))
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

#Criar fórum
def criarForum(forum):
    conexao = obterConexao()
    cursor = conexao.cursor()
    sql = "INSERT INTO forum (titulo,assunto,idaluno) VALUES (%s,%s,%s)"
    cursor.execute(sql, [forum['titulo'], forum['assunto'], forum['idaluno']])
    conexao.commit()
    conexao.close()

#Obtem todos os fóruns
def obterForuns():
    conexao = obterConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM forum ORDER BY id DESC")
    foruns = cursor.fetchall()
    conexao.close()
    return foruns

#Obtem dados de um fórum
def obterForum(idforum):
    conexao = obterConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT forum.titulo, forum.assunto, forum.datahora, aluno.avatar, aluno.nome FROM projetos.forum AS forum INNER JOIN projetos.aluno AS aluno ON forum.idaluno = aluno.id WHERE forum.id = %s", (idforum,))
    forum = cursor.fetchone()
    conexao.close()
    return forum

#Obtem todas as mensagens de um fórum
def obterMensagens(idforum):
    conexao = obterConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT mensagem.mensagem, mensagem.datahora, aluno.avatar, aluno.nome FROM projetos.mensagem_forum AS mensagem INNER JOIN projetos.aluno AS aluno ON mensagem.idaluno = aluno.id WHERE mensagem.idforum = %s", (idforum,))
    mensagens = []
    mensagens = cursor.fetchall()
    conexao.close()
    return mensagens

#Cadastra mensagem em um fórum
def cadastrarMensagem(mensagem):
    conexao = obterConexao()
    cursor = conexao.cursor()
    sql = "INSERT INTO mensagem_forum (mensagem,idforum,idaluno) VALUES (%s,%s,%s)"
    cursor.execute(sql, [mensagem['mensagem'], mensagem['idforum'], mensagem['idaluno']])
    conexao.commit()
    conexao.close()

#Cadastra matrícula em um curso
def cadastrarMatricula(matricula):
    conexao = obterConexao()
    cursor = conexao.cursor()
    sql = "INSERT INTO matricula (idcurso,idaluno) VALUES (%s,%s)"
    cursor.execute(sql, [matricula['idcurso'], matricula['idaluno']])
    conexao.commit()
    conexao.close()

#Busca se o aluno já está matriculado em um curso
def matriculado(idcurso,idaluno):
    conexao = obterConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM matricula WHERE idcurso = %s AND idaluno = %s", (idcurso,idaluno))
    matricula = cursor.fetchall()
    conexao.close()
    return matricula

#Busca a próxima aula de um curso
def proximaAula(idcurso,numero):
    conexao = obterConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM aula WHERE idcurso = %s AND numero > %s LIMIT 1", (idcurso,numero))
    aula = cursor.fetchone()
    conexao.close()
    return aula

#Atualiza cadastro do aluno
def atualizarAluno(aluno,idaluno):
    conexao = obterConexao()
    cursor = conexao.cursor(dictionary=True)
    sql = "UPDATE aluno SET senha = %s, avatar = %s WHERE id = %s"
    cursor.execute(sql, [aluno['senha'], aluno['avatar'], idaluno])
    conexao.commit()
    conexao.close()


#### Página de administrador ####

def insereCurso(curso):
    conexao = obterConexao()
    cursor = conexao.cursor()  
    sql = "INSERT INTO curso (titulo,descricao,idade,quantidade_aulas,idprofessor) VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(sql, [curso['titulo'], curso['descricao'], curso['idade'], curso['quantidade_aulas'], curso['idprofessor']])
    conexao.commit()

def atualizaCurso(curso,id):
    conexao = obterConexao()
    cursor = conexao.cursor(dictionary=True)
    sql = "UPDATE curso SET titulo = %s, descricao = %s, idade = %s, quantidade_aulas = %s, idprofessor = %s WHERE id = %s"
    cursor.execute(sql, [curso['titulo'], curso['descricao'], curso['idade'], curso['quantidade_aulas'], curso['idprofessor'], id])
    conexao.commit()
    conexao.close()

def deletaCurso(id):
    conexao = obterConexao()
    cursor = conexao.cursor(dictionary=True)
    sql = "DELETE FROM curso WHERE id = %s"
    cursor.execute(sql, [id])
    conexao.commit()
    conexao.close()

def insereAula(aula):
    conexao = obterConexao()
    cursor = conexao.cursor()  
    sql = "INSERT INTO aula (titulo,descricao,video,numero,idcurso) VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(sql, [aula['titulo'], aula['descricao'], aula['video'], aula['numero'], aula['idcurso']])
    conexao.commit()

def atualizaAula(aula,id):
    conexao = obterConexao()
    cursor = conexao.cursor(dictionary=True)
    sql = "UPDATE aula SET titulo = %s, descricao = %s, video = %s, numero = %s, idcurso = %s WHERE id = %s"
    cursor.execute(sql, [aula['titulo'], aula['descricao'], aula['video'], aula['numero'], aula['idcurso'], id])
    conexao.commit()
    conexao.close()

def deletaAula(id):
    conexao = obterConexao()
    cursor = conexao.cursor(dictionary=True)
    sql = "DELETE FROM aula WHERE id = %s"
    cursor.execute(sql, [id])
    conexao.commit()
    conexao.close()

#Obtém todos os professores
def obterProfessores():
    conexao = obterConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM professor")
    professores = cursor.fetchall()
    conexao.close()
    return professores
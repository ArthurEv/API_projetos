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

#Obtém todos os cursos disponíveis
def obterCursosDisponiveis():
    conexao = obterConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM curso")
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

print(obterCursosDisponiveis())
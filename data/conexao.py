import mysql.connector

# Todo nome de classe começa com maiuscula
class Conexao:
    def criar_conexao():
        # Criando a conexao
        conexao = mysql.connector.connect(host = "localhost",
                                port = 3306,
                                user = "root",
                                password = "root",
                                database = "dbComentarios")
        
        return conexao
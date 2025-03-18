import mysql.connector

# Todo nome de classe começa com maiuscula
class Conexao:
    def criar_conexao():
        # Criando a conexao
        conexao = mysql.connector.connect(host = "10.110.131.22",
                                port = 3306,
                                user = "3ds",
                                password = "banana",
                                database = "db_feedback")
        
        return conexao
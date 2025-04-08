import mysql.connector

# Todo nome de classe começa com maiuscula
class Conexao:
    def criar_conexao():
        # Criando a conexao
        conexao = mysql.connector.connect(host = "bdgodofredo-alexstocco-93db.b.aivencloud.com",
                                port = 27974,
                                user = "3ds",
                                password = "banana",
                                database = "db_feedback")
        
        return conexao
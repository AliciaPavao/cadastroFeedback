import datetime
from data.conexao import Conexao
from hashlib import sha256

class Usuario:
    def cadastrar_usuario (usuario, nome, senha):
         
        senha = sha256(senha.encode()).hexdigest()

        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor()

        sql = """INSERT INTO tb_usuarios
                (login, nome, senha)
                VALUES
                    (%s,%s,%s)"""
        valores=(usuario, nome, senha)

        cursor.execute(sql, valores)

        conexao.commit()

        # Fecho a conexao com o banco
        cursor.close()
        conexao.close() 

    def logar(usuario, senha):
         
        senha = sha256(senha.encode()).hexdigest()

        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor()

        SQL = """SELECT * FROM tb_usuarios
        WHERE login = %s
        AND BINARY senha = %s ;"""
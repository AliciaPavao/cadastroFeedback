import datetime

from data.conexao import Conexao
from hashlib import sha256
from flask import session

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

        cursor = conexao.cursor(dictionary = True)

        SQL = """SELECT login, nome FROM tb_usuarios
        WHERE login = %s
        AND BINARY senha = %s ;"""

        valores = (usuario, senha)

        cursor.execute(SQL, valores)

        resultado = cursor.fetchone()
        
        cursor.close() # Põe o cursor em cima do conexao 
        conexao.close()
        
        if resultado:
            session['usuario'] = resultado['login']
            session['nome_usuario'] = resultado['nome']
            return True
        else:
            return False

    def logoff():
        session.clear() 
      

    

import datetime
from data.conexao import Conexao

class Mensagem:
    def cadastrar_mensagem(usuario, mensagem):
        data_hora = datetime.datetime.today()
    
        #variavel - conexao arquivo
        conexao = Conexao.criar_conexao()
        
        cursor = conexao.cursor()

        # Criando o sql que será executado
        sql = """INSERT INTO tbcomentarios
                (nome, data_hora, comentario)
                VALUES
                    (%s,%s,%s)"""
        valores=(usuario, data_hora, mensagem)

        # Executando o comando sql
        cursor.execute(sql, valores)

        # Confirmo a alteração
        conexao.commit()

        # Fecho a conexao com o banco
        cursor.close()
        conexao.close() 
import datetime
from data.conexao import Conexao

class Mensagem:
    def cadastrar_mensagem(usuario, mensagem):
        data_hora = datetime.datetime.today()
    
        #variavel - conexao arquivo
        conexao = Conexao.criar_conexao()
        
        cursor = conexao.cursor()

        # Criando o sql que será executado
        sql = """INSERT INTO tb_comentarios
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

    def recuperar_mensagens():
        # Criando a conexão
        conexao = Conexao.criar_conexao()

        # O cursor será responsavel por manipular o banco de dados
        cursor = conexao.cursor(dictionary = True)

        # Criando o SQL que será executado
        sql = """select nome, 
                        comentario,
                        data_hora,
                        cod_comentario,
                        curtidas
                        from tb_comentarios"""
        
        # Executando o comando sql
        cursor.execute(sql)

        # Recuperando os dados e guardando em uma variavel
        resultado = cursor.fetchall()

        # Fecho a conexão com o banco
        conexao.close()

        return resultado
    
    def deletar_mensagem(codigo):
      
    
        #variavel - conexao arquivo
        conexao = Conexao.criar_conexao()
        
        cursor = conexao.cursor()

        # Criando o sql que será executado
        sql = """DELETE FROM tb_comentarios WHERE cod_comentario = %s"""
        valores = (codigo,)

        # Executando o comando sql
        cursor.execute(sql, valores)

        # Confirmo a alteração
        conexao.commit()

        # Fecho a conexao com o banco
        cursor.close()
        conexao.close()  

    def aumentar_likes(codigo):
       #variavel - conexao arquivo
        conexao = Conexao.criar_conexao()
        
        cursor = conexao.cursor()

        # Criando o sql que será executado
        sql = """UPDATE tb_comentarios SET curtidas = curtidas + 1 WHERE cod_comentario = %s"""
        valores = (codigo,)

        # Executando o comando sql
        cursor.execute(sql, valores)

        # Confirmo a alteração
        conexao.commit()

        # Fecho a conexao com o banco
        cursor.close()
        conexao.close() 
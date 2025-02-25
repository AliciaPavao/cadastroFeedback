from flask import Flask, render_template, request
import datetime
import mysql.connector
app = Flask(__name__)

@app.route("/")
def pagina_principal():
    return render_template("pagPrincipal.html")

@app.route("/post/mensagem", methods=["POST"])
def cadastrarComentarios():
    usuario = request.form.get("usuario")
    mensagem = request.form.get("mensagem")
    data_hora = datetime.datetime.today()
    
    conexao = mysql.connector.connect(host = "localhost",
                            port = 3306,
                            user = "root",
                            password = "root",
                            database = "dbComentarios")
    
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

    return render_template("pagPrincipal.html")

# Cadastrando as coisas no banco de dados

app.run(debug = True)
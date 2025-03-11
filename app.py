from flask import Flask, render_template, request
import datetime
import mysql.connector
# Importando a pasta o arquivo e a classe
from data.conexao import Conexao
from model.control_mensagem import Mensagem
app = Flask(__name__)

@app.route("/")
def pagina_principal():
    return render_template("pagPrincipal.html")

@app.route("/post/mensagem", methods=["POST"])
def cadastrarComentarios():
    usuario = request.form.get("usuario")
    mensagem = request.form.get("mensagem")

    # Cadastrando a mensagem usando a Classe Mensagem
    Mensagem.cadastrar_mensagem(usuario, mensagem)
    
    # Redireciona para o index
    return render_template("pagPrincipal.html")

# Cadastrando as coisas no banco de dados

app.run(debug = True)
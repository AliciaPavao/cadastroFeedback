from flask import Flask, render_template, request, redirect
import datetime
import mysql.connector
# Importando a pasta o arquivo e a classe
from data.conexao import Conexao
from model.control_mensagem import Mensagem
app = Flask(__name__)

@app.route("/")
def pagina_principal():
    # Recuperar as mensagens
    mensagens = Mensagem.recuperar_mensagens()

    # Enviar as mensagens para o template
    return render_template("pagPrincipal.html", mensagens = mensagens)

@app.route("/post/mensagem", methods=["POST"])
def cadastrarComentarios():
    usuario = request.form.get("usuario")
    mensagem = request.form.get("mensagem")

    # Cadastrando a mensagem usando a Classe Mensagem
    Mensagem.cadastrar_mensagem(usuario, mensagem)
    
    # Redireciona para o index
    return render_template("pagPrincipal.html")

@app.route("/delete/mensagem/<codigo>")
def delete_mensagem(codigo):
    Mensagem.deletar_mensagem(codigo)
    return redirect("/")

@app.route("/put/curtidas/<codigo>")
def aumentar_likes(codigo):
    Mensagem.aumentar_likes(codigo)
    return redirect("/")

app.run(debug = True)
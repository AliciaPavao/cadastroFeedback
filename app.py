from flask import Flask, render_template, request, redirect
import datetime
import mysql.connector
# Importando a pasta o arquivo e a classe
from data.conexao import Conexao
from model.controler_mensagem import Mensagem
from model.controler_usuario import Usuario
from flask import session

app = Flask(__name__)

app.secret_key = "Godofredolindo"

@app.route("/cadastro")
def pagina_pagCadastro():
    return render_template(("pagCadastro.html"))

@app.route("/")
def pagina_login():
    return render_template(("pagLogin.html"))

@app.route("/post/login", methods=["POST"])
def post_logar():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    #class  #def
    esta_logado = Usuario.logar(usuario, senha)

    if esta_logado:
        return redirect("/comentario")
    else: 
        return redirect("/")

@app.route("/comentario")
def pagina_principal():

    if 'usuario' in session:

        # Recuperar as mensagens
        mensagens = Mensagem.recuperar_mensagens()

        # Enviar as mensagens para o template
        return render_template("pagPrincipal.html", mensagens = mensagens)
    else:
        return redirect("/")

@app.route("/post/mensagem", methods=["POST"])
def cadastrarComentarios():
    usuario = request.form.get("usuario")
    mensagem = request.form.get("mensagem")

    # Cadastrando a mensagem usando a Classe Mensagem
    Mensagem.cadastrar_mensagem(usuario, mensagem)
    
    # Redireciona para o index
    return redirect("/comentario")

@app.route("/delete/mensagem/<codigo>")
def delete_mensagem(codigo):
    Mensagem.deletar_mensagem(codigo)
    return redirect("/comentario")

@app.route("/put/curtidas/<codigo>")
def aumentar_likes(codigo):
    Mensagem.aumentar_likes(codigo)
    return redirect("/comentario")

@app.route("/remove/curtidas/<codigo>")
def diminuir_likes(codigo):
    Mensagem.diminuir_likes(codigo)
    return redirect("/comentario")

@app.route("/post/cadastro", methods=["POST"])
def cadastrarUsuario():
    
    usuario = request.form.get("usuario")
    nome = request.form.get("nome")
    senha = request.form.get("senha")

    # Cadastrando a mensagem usando a Classe Mensagem
    Usuario.cadastrar_usuario(usuario, nome, senha)
    
    # Redireciona para o index
    return redirect("/")

app.run(debug = True)
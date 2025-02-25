from flask import Flask
app = Flask(__name__)

@app.route("/")
def pagina_principal():
    return "Página principal"

app.run(debug = True)
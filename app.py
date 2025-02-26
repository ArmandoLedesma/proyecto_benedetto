from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  

@app.route("/iniciar_sesion")
def login():
    return render_template("login.html")

@app.route("/registro")
def registrarse():
    return render_template("registro.html")

@app.route("/recuperacion")
def recuperar():
    return render_template("recuperacion.html")

if __name__ == "__main__":
    app.run(debug=True)

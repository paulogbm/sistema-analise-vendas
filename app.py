from flask import Flask, render_template, request
from services.analise import analisar_csv
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():

    return render_template(
        "dashboard.html",
        total_vendas=0,
        produto_lider="-",
        produto_menor="-",
        outliers=0
    )

@app.route("/upload", methods=["POST"])
def upload():

    arquivo = request.files["arquivo"]

    if arquivo:

        caminho = os.path.join(
            UPLOAD_FOLDER,
            arquivo.filename
        )

        arquivo.save(caminho)

        resultado = analisar_csv(caminho)

        return render_template(
            "dashboard.html",
            total_vendas=resultado["total_vendas"],
            produto_lider=resultado["produto_lider"],
            produto_menor=resultado["produto_menor"],
            outliers=resultado["outliers"]
        )

    return "Erro ao enviar arquivo"

if __name__ == "__main__":
    app.run(debug=True)
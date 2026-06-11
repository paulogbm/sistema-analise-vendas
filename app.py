from flask import Flask, render_template, request, redirect, url_for, flash, session
from services.analise import analisar_csv
import os
import sqlite3

app = Flask(__name__)


app.secret_key = "chave_secreta_para_testes"

UPLOAD_FOLDER = "uploads"


os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ================= CONFIGURAÇÃO DO BANCO DE DADOS (SQLite) =================
DB_NAME = "vendas.db"

def obter_conexao():
    
    conexao = sqlite3.connect(DB_NAME)
    
    conexao.row_factory = sqlite3.Row
    return conexao

def inicializar_banco():
    conexao = obter_conexao()
    
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
    """)
    
    
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = 'admin@teste.com'")
    if not cursor.fetchone():
        conexao.execute("""
            INSERT INTO usuarios (nome, email, senha) 
            VALUES ('Administrador', 'admin@teste.com', '1234')
        """)
    
    conexao.commit()
    conexao.close()


inicializar_banco()
    

# ================= ROTAS DE AUTENTICAÇÃO (LOGIN) =================

# 1. Tela de Login (Página Inicial)
@app.route("/")
def login():
    
    if "usuario_id" in session:
        return redirect(url_for("dashboard"))
    return render_template("login.html")



@app.route("/login", methods=["POST"])
def acao_login():
    email = request.form.get("email")
    senha = request.form.get("password")
    
    conexao = obter_conexao()
   
    usuario = conexao.execute("SELECT * FROM usuarios WHERE email = ?", (email,)).fetchone()
    conexao.close()
    
   
    if usuario and usuario["senha"] == senha:
       
        session["usuario_id"] = usuario["id"]
        session["usuario_nome"] = usuario["nome"]
        return redirect(url_for("dashboard"))
    else:
       
        flash("Usuário ou senha incorretos!")
        return redirect(url_for("login"))



@app.route("/logout")
def logout():
    
    session.clear()
    return redirect(url_for("login"))


# ================= ROTAS DO DASHBOARD (ANÁLISE DE PRODUTOS) =================


@app.route("/dashboard")
def dashboard():
    
    if "usuario_id" not in session:
        flash("Acesso negado! Por favor, faça login primeiro.")
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        total_vendas=0,
        produto_lider="-",
        produto_menor="-",
        outliers=0,
        produtos=[],
        valores=[]
    )


# Upload e processamento do CSV
@app.route("/upload", methods=["POST"])
def upload():
    
    if "usuario_id" not in session:
        return redirect(url_for("login"))

    
    if "arquivo" not in request.files:
        flash("Nenhum arquivo enviado!")
        return redirect(url_for("dashboard"))

    arquivo = request.files["arquivo"]

    if arquivo and arquivo.filename != "":
        
        if not arquivo.filename.endswith('.csv'):
            flash("Apenas arquivos no formato CSV são aceitos!")
            return redirect(url_for("dashboard"))

        caminho = os.path.join(UPLOAD_FOLDER, arquivo.filename)
        arquivo.save(caminho)

        try:
            resultado = analisar_csv(caminho)
            
            return render_template(
                "dashboard.html",
                total_vendas=resultado["total_vendas"],
                produto_lider=resultado["produto_lider"],
                produto_menor=resultado["produto_menor"],
                outliers=resultado["outliers"],
                produtos=resultado["produtos"],
                valores=resultado["valores"]
            )
        except Exception:
            flash("Erro ao processar o arquivo CSV. Verifique a consistência dos dados.")
            return redirect(url_for("dashboard"))

    return redirect(url_for("dashboard"))


# ================= ROTAS DO CRUD DE USUÁRIOS (Requisito do Professor) =================


@app.route("/usuarios")
def usuarios():
    
    if "usuario_id" not in session:
        flash("Acesso negado! Por favor, faça login primeiro.")
        return redirect(url_for("login"))

    conexao = obter_conexao()
    
    usuarios_banco = conexao.execute("SELECT * FROM usuarios").fetchall()
    conexao.close()
    return render_template("upload.html", lista_usuarios=usuarios_banco)



@app.route("/usuarios/novo", methods=["POST"])
def usuarios_novo():
    
    if "usuario_id" not in session:
        return redirect(url_for("login"))

    nome = request.form.get("nome")
    email = request.form.get("email")
    senha = request.form.get("senha")

    if nome and email and senha:
        conexao = obter_conexao()
        try:
            
            conexao.execute(
                "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
                (nome, email, senha)
            )
            conexao.commit()
        except sqlite3.IntegrityError:
            
            flash("Este e-mail já está cadastrado por outro usuário!")
        finally:
            conexao.close()
        
    return redirect(url_for("usuarios"))



@app.route("/usuarios/deletar/<int:id>")
def usuarios_deletar(id):
    
    if "usuario_id" not in session:
        return redirect(url_for("login"))

    
    if id == 1:
        flash("O usuário administrador mestre não pode ser deletado!")
        return redirect(url_for("usuarios"))
        
    conexao = obter_conexao()
    
    conexao.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()
    return redirect(url_for("usuarios"))


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for, flash
from services.analise import analisar_csv
import os

app = Flask(__name__)

# CHAVE SECRETA: Necessária para usar o 'flash' (mensagens de erro/sucesso)
app.secret_key = "chave_secreta_para_testes"

UPLOAD_FOLDER = "uploads"

# Cria a pasta uploads caso não exista
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ================= SIMULAÇÃO DO BANCO DE DATOS (Para o CRUD) =================
# Como o SQLite está em desenvolvimento, usamos esta lista global na memória.
# Ela permite que você Cadastre e Exclua usuários de verdade enquanto testa!
USUARIOS_BANCO = [
    {"id": 1, "nome": "Ana Carolina", "email": "ana@salesvision.com"},
    {"id": 2, "nome": "Paulo Gustavo", "email": "paulo@salesvision.com"},
    {"id": 3, "nome": "Débora Valeriano", "email": "debora@salesvision.com"}
]


# ================= ROTAS DE AUTENTICAÇÃO (LOGIN) =================

# 1. Tela de Login (Página Inicial)
@app.route("/")
def login():
    return render_template("login.html")


# 2. Ação de Logar (Processa o formulário de login)
@app.route("/login", methods=["POST"])
def acao_login():
    email = request.form.get("email")
    senha = request.form.get("password")
    
    # Validação simples para permitir o avanço para o Dashboard nos testes
    if email == "admin@teste.com" and senha == "1234":
        return redirect(url_for("dashboard"))
    else:
        # Envia o aviso vermelho para a tela de login
        flash("Usuário ou senha incorretos!")
        return redirect(url_for("login"))


# 3. Ação de Sair (Logout)
@app.route("/logout")
def logout():
    return redirect(url_for("login"))


# ================= ROTAS DO DASHBOARD (ANÁLISE DE PRODUTOS) =================

# Exibe o Dashboard limpo
@app.route("/dashboard")
def dashboard():
    return render_template(
        "dashboard.html",
        total_vendas=0,
        produto_lider="-",
        produto_menor="-",
        outliers=0,
        produtos=[],
        valores=[]
    )


# Upload e processamento do CSV (Mantido a lógica original dos seus amigos)
@app.route("/upload", methods=["POST"])
def upload():
    # Verifica se o arquivo foi enviado na requisição
    if "arquivo" not in request.files:
        flash("Nenhum arquivo enviado!")
        return redirect(url_for("dashboard"))

    arquivo = request.files["arquivo"]

    if arquivo and arquivo.filename != "":
        # Regra de integridade: Valida se a extensão é .csv (critério do plano de testes)
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
                outliers=resultado["outliers"]
            )
        except Exception:
            flash("Erro ao processar o arquivo CSV. Verifique a consistência dos dados.")
            return redirect(url_for("dashboard"))

    return redirect(url_for("dashboard"))


# ================= ROTAS DO CRUD DE USUÁRIOS (Requisito do Professor) =================

# 1. READ: Listar usuários cadastrados
@app.route("/usuarios")
def usuarios():
    return render_template("upload.html", lista_usuarios=USUARIOS_BANCO)


# 2. CREATE: Cadastrar novo usuário
@app.route("/usuarios/novo", methods=["POST"])
def usuarios_novo():
    nome = request.form.get("nome")
    email = request.form.get("email")
    senha = request.form.get("senha") # Em um sistema real, aplicaríamos hash aqui

    if nome and email and senha:
        # Descobre o próximo ID incremental
        novo_id = max([u["id"] for u in USUARIOS_BANCO]) + 1 if USUARIOS_BANCO else 1
        
        # Salva o novo dicionário na nossa lista simulada
        USUARIOS_BANCO.append({
            "id": novo_id,
            "nome": nome,
            "email": email
        })
        
    return redirect(url_for("usuarios"))


# 3. DELETE: Excluir usuário pelo ID
@app.route("/usuarios/deletar/<int:id>")
def usuarios_deletar(id):
    global USUARIOS_BANCO
    # Filtra a lista mantendo apenas quem NÃO tem o ID clicado
    USUARIOS_BANCO = [u for u in USUARIOS_BANCO if u["id"] != id]
    return redirect(url_for("usuarios"))


if __name__ == "__main__":
    app.run(debug=True)
import pytest
from app import app, obter_conexao

@pytest.fixture
def cliente():
    
    app.config["TESTING"] = True
    app.config["WTF_CSRF_ENABLED"] = False 
    
    
    with app.test_client() as cliente:
        yield cliente

def test_rota_login_carrega_com_sucesso(cliente):
    
    resposta = cliente.get("/")
    
    
    assert resposta.status_code == 200
    
    
    assert b"SalesVision" in resposta.data or b"Login" in resposta.data

def test_bloqueio_api_dashboard_sem_sessao(cliente):
    
    resposta = cliente.get("/dashboard")
    
    
    assert resposta.status_code == 302
    assert "/" in resposta.headers["Location"]

def test_api_login_com_sucesso(cliente):
    
    dados_login = {
        "email": "admin@teste.com",
        "password": "1234"
    }
    resposta = cliente.post("/login", data=dados_login)
    
    
    assert resposta.status_code == 302
    assert "/dashboard" in resposta.headers["Location"]

def test_api_login_invalido(cliente):
    
    dados_errados = {
        "email": "usuario_fantasma@teste.com",
        "password": "999"
    }
    resposta = cliente.post("/login", data=dados_errados)
    
    
    assert resposta.status_code == 302
    assert resposta.headers["Location"] == "/" or resposta.headers["Location"] == "http://localhost/"
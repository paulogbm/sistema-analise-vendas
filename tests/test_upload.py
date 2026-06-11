import pytest
import os
from playwright.sync_api import sync_playwright

BASE_URL = "http://127.0.0.1:5000"

@pytest.fixture
def criar_csv_teste():
    caminho_csv = "tests/vendas_e2e_teste.csv"
    conteudo = (
        "produto,valor,quantidade\n"
        "Notebook,4500.00,1\n"
        "Mouse Gamer,150.00,1\n"
        "Teclado Mecanico,350.00,1\n"
        "Monitor 4K,2500.00,1\n"
    )
    with open(caminho_csv, "w", encoding="utf-8") as f:
        f.write(conteudo)
    
    yield os.path.abspath(caminho_csv)
    
    if os.path.exists(caminho_csv):
        os.remove(caminho_csv)

def test_fluxo_completo_upload_e_tabela(criar_csv_teste):
    with sync_playwright() as p:
       
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        
     
        page.goto(f"{BASE_URL}/")
        
       
        page.fill("input[name='email']", "admin@teste.com")
        page.fill("input[name='password']", "1234")
        page.click("text=Acessar Plataforma")
        
        
        page.wait_for_url(f"{BASE_URL}/dashboard")
        
        
        page.set_input_files("input[id='arquivo_csv']", criar_csv_teste)
        
       
        page.click("text=Processar Dados")
        
      
        tabela_carregada = page.wait_for_selector("text=Notebook", state="visible", timeout=5000)
        assert tabela_carregada
        
        
        dados_valor = page.locator("text=4500")
        assert dados_valor.is_visible()
        
        browser.close()
import pytest
import os
import pandas as pd
from services.analise import analisar_csv


@pytest.fixture
def csv_temporario():
    caminho_arquivo = "tests/temporario_vendas.csv"
    
    
    conteudo_csv = (
        "produto,valor,quantidade\n"
        "Notebook,4000.00,2\n"      
        "Mouse,100.00,10\n"         
        "Teclado,200.00,1\n"        
        "SuperComputador,50000.00,1\n" 
    )
    
    
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write(conteudo_csv)
        
   
    yield caminho_arquivo
    
    if os.path.exists(caminho_arquivo):
        os.remove(caminho_arquivo)



def test_calculos_analise_csv(csv_temporario):
    
    resultado = analisar_csv(csv_temporario)
    
   
    assert resultado["total_vendas"] == 54300.0
    
    
    assert resultado["produto_lider"] == "Mouse"
    
    
    assert resultado["produto_menor"] == "Teclado"
    
    
    assert resultado["outliers"] == 1
    
    
    assert len(resultado["produtos"]) == 4
    assert len(resultado["valores"]) == 4
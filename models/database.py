import sqlite3

def criar_banco():

    conexao = sqlite3.connect("database.db")

    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS historico (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            arquivo TEXT,
            receita REAL,
            produto_lider TEXT,
            produto_menor TEXT,
            outliers INTEGER
        )
    """)

    conexao.commit()
    conexao.close()
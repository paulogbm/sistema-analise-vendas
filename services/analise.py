import pandas as pd

def analisar_csv(caminho):

    df = pd.read_csv(caminho)

    total_vendas = df["valor"].sum()

    produto_lider = df.loc[
        df["quantidade"].idxmax(),
        "produto"
    ]

    produto_menor = df.loc[
        df["quantidade"].idxmin(),
        "produto"
    ]

    media = df["valor"].mean()

    outliers = df[df["valor"] > media * 2]

    quantidade_outliers = len(outliers)

    produtos = df["produto"].tolist()
    valores = df["valor"].tolist()

    return {
        "total_vendas": round(total_vendas, 2),
        "produto_lider": produto_lider,
        "produto_menor": produto_menor,
        "outliers": quantidade_outliers,
        "produtos": produtos,
        "valores": valores
    }
import pandas as pd

df_dados_incompletos = pd.DataFrame([
    {
        "nome": "João de Menezes",
        "cpf": "123.456.789-00",
        "salario": "R$ 5800"
    },
    {
        "nome": "Victor Sousa",
        "cpf": 11122233344,
        "salario": True
    },
    {
        "nome": "Marcelo Oliveira",
        "cpf": "000 333 333-99",
        "salario": 1000
    }
])

df_dados_incompletos.to_csv("dados_incompletos.csv", index=False)

dados = pd.read_csv("dados_incompletos.csv",
                    dtype={"cpf": "string",
                           "salario": "string"})

# dados["cpf_formatado"] = (dados["cpf"]
#                           .str.replace(".", "")
#                           .str.replace("-", "")
#                           .str.replace(" ", ""))

dados["cpf_formatado"] = dados["cpf"].str.replace(r"\D", "", regex=True)
dados["salario_formatado"] = (dados["salario"]
                              .str.replace(r"[^\d,.\-]", "", regex=True)
                              .str.replace(r".", "", regex=False)
                              .str.replace(r",",".", regex=False)
                              )

dados["salario_formatado"] = pd.to_numeric(
    dados["salario_formatado"], errors="coerce"
)

dados["cpf_formatado"] = pd.to_numeric(
    dados["cpf_formatado"], errors="coerce"
)

print(dados.to_string())
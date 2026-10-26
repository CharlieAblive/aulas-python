import pandas as pd

df_dados_incompletos = pd.DataFrame([
    {
        "nome": "",
        "cpf": "12345678978",
        "salario": "asd asdasdasdvadvas",
        "telefone": "# $ *(){"
    },
    {
        "nome": "Victor Sousa",
        "cpf": 11122233344,
        "salario": "5.000,88",
        "telefone": "+55 62 12345-1234"
    },
    {
        "nome": "",
        "cpf": "000 333 333-99",
        "salario": 1000.9900,
        "telefone": "63 1111-1111"
    }
])

df_dados_incompletos.to_csv("dados_incompletos.csv", index=False)

dados = pd.read_csv("dados_incompletos.csv",
                    dtype={"cpf": "string",
                           "salario": "string",
                           "telefone": "string"})

# dados["cpf_formatado"] = (dados["cpf"]
#                           .str.replace(".", "")
#                           .str.replace("-", "")
#                           .str.replace(" ", ""))

dados.insert(2, "cpf_formatado", dados["cpf"].str.replace(r"\D", "", regex=True))
dados.insert(3, "cpf_validado", dados["cpf_formatado"].str.fullmatch(r"\d{11}"))

# Realiza a limpeza com regex
dados_salario_limpo = (dados["salario"]
                       .str.replace(r"[^\d,.\-]", "", regex=True)
                       .str.replace(r"\.(?=\d{3}(?:\.|,|$))", "", regex=True)
                       .str.replace(r",", ".", regex=False))

# Converte para float e força erros a virarem NaN
dados_salario_formatados = pd.to_numeric(dados_salario_limpo, errors='coerce')

# Opcional: Se preferir que os salários inválidos/vazios sejam 0 em vez de NaN, descomente a linha abaixo:
# dados_salario_formatados = dados_salario_formatados.fillna(0)

dados.insert(5, "salario_formatado", dados_salario_formatados)

print(dados["salario_formatado"])

print(dados["salario_formatado"].sum())

dados_telefone_formatados = (
    dados["telefone"].str.replace(r"\D", "", regex=True)
)

dados.insert(7, "telefone_formatado", dados_telefone_formatados)
dados["telefone_validado"] = (dados['telefone_formatado'].str.fullmatch(r"\d{10,11}"))

print(dados.to_string())

print("\n--- Iniciando a correção interativa de dados vazios ---\n")

for index, row in dados.iterrows():

    # 1. Verificando e corrigindo a coluna 'nome'
    # pd.isna() checa se é NaN/<NA>, e pd.Series(row['nome']).str.strip() == "" checa strings vazias
    if pd.isna(row["nome"]) or str(row["nome"]).strip() == "":
        while True:
            novo_nome = input(f"-> A linha {index} está com o 'nome' vazio. Digite um nome válido: ")
            if novo_nome.strip() != "":
                dados.at[index, "nome"] = novo_nome
                break
            print("O nome não pode ficar em branco. Tente novamente.")

    # 2. Verificando e corrigindo a coluna 'salario_formatado'
    if pd.isna(row["salario_formatado"]):
        nome_atual = dados.at[index, "nome"]
        while True:
            novo_salario = input(
                f"-> O salário de '{nome_atual}' (linha {index}) está vazio. Digite um valor numérico (ex: 1500.50): ")
            try:
                # Tenta converter a entrada do usuário para float
                dados.at[index, "salario_formatado"] = float(novo_salario)
                break
            except ValueError:
                print("Valor inválido! Digite apenas números, usando ponto para decimais.")

print("\n--- Correção concluída ---\n")
print(dados.to_string())
import pandas as pd

df = pd.read_csv("funcionarios.csv",sep=";")
print("=== TODA A BASE DE DADOS ===")
print(df.columns.tolist())  # mostra todas as colunas da base de dados em lista
# primeiro filtro
filtro_salarios = df[
    (df['salario'] < 3000) |
    (df['salario'] > 5000) |
    (df['salario'] == 3100)
]
print("\n=== FILTRO POR SALARIOS ===")
print(filtro_salarios)

# segundo filtro
filtro_cargos = df[
    (df['cargo'] == 'Analista de Dados') |
    (df['cargo'] == 'Analista de Sistemas') |
    (df['cargo'] == 'Desenvolvedor Java') |
    (df['cargo'] == 'Cientista de Dados')
]
print("\n=== FILTRO POR CARGOS ===")
print(filtro_cargos)

# terceirro filtro
filtro_salario_cargo = df[
    df['salario'] > 6000
]
print("\n=== FILTRO POR CARGOS E SALARIOS ===")
print(filtro_salario_cargo[
        ['nome', 'cargo']
      ])

# quarto filtro
filtro_por_id = df[
    (df['id'] % 2 == 0)
]
print("\n=== FILTRO POR ID ===")
print(filtro_por_id)

# criando arquivo com os dados filtrados
filtro_salario_cargo.to_csv("filtro_por_salario_e_cargo.csv",
                        index=False,
                        encoding='utf-8',
                        sep="|")

lendo_arquivo_separado = pd.read_csv("filtro_por_salario_e_cargo.csv",
                                     sep="|")
print(lendo_arquivo_separado)
print(lendo_arquivo_separado["nome"])
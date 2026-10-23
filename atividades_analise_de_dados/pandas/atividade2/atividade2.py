import pandas as pd

# base_de_dados = "../atividade1/funcionarios.csv"
base_de_dados = r"C:\TESTES\funcionarios.csv"
df = pd.read_csv(base_de_dados, sep=";")
print(df.columns.tolist()) # lista todas as colunas do arquivo

# filtrando dados com salario acima de 6000
salarios_altos = df[ # variavel com dados filtrados
    (df["salario"] > 6000)
]
# escrevendo os dados filtrado em csv
salarios_altos.to_csv("cargos_altos.csv", index=False, sep=";")
df_filtrado = pd.read_csv("cargos_altos.csv", sep=";")
print(df_filtrado)

novo_funcionario = [{
    "id": 100,
    "nome": "João de Menezes",
    "salario": 150000,
    "cargo": "Instrutor"
},
{
    "id": 101,
    "nome": "Victor Sousa",
    "salario": 200000,
    "cargo": "Interpret"
}
]
df_novo_funcionario = pd.DataFrame(novo_funcionario) # precisa ser DF para ter a concatenação
df_filtrado = pd.concat([df_filtrado, df_novo_funcionario], ignore_index=True)

# criando uma nova coluna
# OBS: precisa ter o mesmo tamanho de linhas do documento
df_filtrado['tempo_empresa'] = [12, 1, 2, 6, 12, 9, 999]
print(df_filtrado)

# apagando linhas pelo index
df_filtrado = df_filtrado.drop(index=0)
df_filtrado = df_filtrado.drop(index=1)

# nova_linha
novo_funcionario = [{
    "id": 200,
    "nome": "Lucas",
    "salario": 1500,
    "cargo": "Estagiário",
    "tempo_empresa": 3
}]


df_novo_funcionario = pd.DataFrame(novo_funcionario)
df_filtrado = pd.concat([df_filtrado, df_novo_funcionario], ignore_index=True)
print(df_filtrado)

#sobreescrevendo o arquivo "cargos_altos.csv"
df_filtrado.to_csv("cargos_altos.csv", index=False, sep=";")

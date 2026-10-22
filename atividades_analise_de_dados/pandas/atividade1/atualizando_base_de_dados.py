import pandas as pd

df = pd.read_csv("funcionarios.csv", sep=";")
df = df.rename(columns={
    'id': "identificador",
    "nome": "funcionario"
})
# print(df[['funcionario', 'identificador']])
novo_funcionario = [
    {
        'identificador': 31,
        'funcionario': "João de Menezes",
        'salario': 100000.0,
        'cargo': "Instrutor SENAI"
    }
]

novo_funcionario = pd.DataFrame(novo_funcionario)
mais_um_funcionario = pd.DataFrame([{
    'identificador': 32,
    'funcionario': "Victor Sousa",
    'salario': 1000.0,
    'cargo': "Interpret SENAI"
}])

df = pd.concat([df, novo_funcionario, mais_um_funcionario], ignore_index=True)
df = df.drop(df[df['identificador'] == 31].index)

df.loc[df['identificador'] == 2, ["funcionario"]] = ["Bruno da Silva"]
df.loc[df['identificador'] == 1, ["funcionario", "salario", "cargo"]] = [
    "Ana Maria",10000.00, "CEO"
]
print(df)
df.to_csv("funcionarios.csv",sep=";",index=False)
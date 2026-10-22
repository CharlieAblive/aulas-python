import pandas as pd

print("LENDO DADOS SALVOS COM LISTA")
df = pd.read_csv("dados_da_lista.csv")

print(df) # IMPRIMIR TODA A BASE DE DADOS
print(df[["nome", 'idade']]) # filtra por coluna
print(df["nome"]) # imprime uma coluna como SERIE
print(df[df["idade"] > 25]) # imprime com condição numérica
print(df[df['nome'] == "Katia"]) # imprime com comparativo de str

nome = input("Digite um nome que queira procurar na base de dados: ")
print(df[df["nome"] == nome])

idade = int(input("Digite um limite de idade: "))
print(df[df["idade"] == idade])

# Buscando com operar and
print("ENTRE 20 E 30 ANOS")
print(df[
          (df['idade'] > 20) & (df['idade'] < 30)
      ])

# Buscando com operar or
print("IGUAL A 20, 33, 40 OU 19 ANOS")
print(df[
          (df['idade'] == 20) |
          (df['idade'] == 33) |
          (df['idade'] == 40) |
          (df['idade'] == 19)
      ])

# Usando o not

# Buscando com operar and
print("NÃO SEJA MAIOR DO QUE 20")
print(df[
          -(df['idade'] > 20)
      ])

df.to_csv("dados_pandas.csv", index=False)
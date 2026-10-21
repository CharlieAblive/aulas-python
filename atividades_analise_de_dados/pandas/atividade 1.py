import pandas

df = pandas.read_csv("funcionarios.csv",
                     sep=";")

print(df.iloc[0]) # busca pelo index da lista com o read_csv
import pandas as pd
texto = [{
    "nome": "João",
    "idade": 31
}]
df = pd.DataFrame(texto)
df.to_csv("meu_nome.csv", index=False, sep=";")
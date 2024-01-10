import pandas as pd

url = "https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv"

df = pd.read_csv(url, sep=";")

# Quantidade de linhas e colunas
linhas, colunas = df.shape
print(f"O Dataframe possui {linhas} linhas e {colunas} colunas\n")

# Colunas disponíveis no Dataframe
nomes_das_colunas = [column for column in df.columns]
print("O Dataframe possui as seguintes colunas:")
print(f" => {', '.join([coluna for coluna in nomes_das_colunas])}\n")

# Tipos de dado por coluna
print("O tipo por coluna do Fataframe é:")
print(df.dtypes)

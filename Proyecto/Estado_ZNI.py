import pandas as pd
df = pd.read_csv("CURSO_IA\Proyecto\Estado_ZNI.csv")
print(df.count())
print("VISTA INICIAL DEL DATAFRAME")
print(df.head())
print("\nVALORES NULOS POR COLUMNA")
print(df.isnull().sum())
print(df.describe())

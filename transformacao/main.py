import pandas as pd
import sqlite3

#df = pd.read_csv("/../data/data.csv")
df = pd.read_csv(r"C:\Users\diogo\OneDrive\Área de Trabalho\GitHub\scrapy_empregos\data\data.csv")
df["titulo"] = df["titulo"].str.lower()
df = df[df["titulo"].str.contains("analista|dados|dado|b.i.|b.i|power|inteligência|inteligencia|business|intelligence")]
df.to_excel("C:\\Users\\diogo\\Downloads\\empregos.xlsx", sheet_name = "empregos")
print(df)
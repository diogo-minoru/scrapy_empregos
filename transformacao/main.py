import pandas as pd

df = pd.read_csv("/../data/data.csv")
df["titulo"] = df["titulo"].str.lower()
df = df[df["titulo"].str.contains("analista|dados|dado|b.i.|b.i|power|inteligência|inteligencia|business|intelligence")]
df.to_excel("empregos.xlsx", sheet_name = "empregos")
print(df)
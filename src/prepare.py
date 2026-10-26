import pandas as pd

df = pd.read_csv("data/patients.csv")
df["sexe"] = (df["sexe"] == "M").astype(int)
df["risque_eleve"] = (df["cholesterol"] >= 240).astype(int)
df = df.drop(columns=["id"])
df.to_csv("data/processed.csv", index=False)
print("processed.csv :", df.shape)

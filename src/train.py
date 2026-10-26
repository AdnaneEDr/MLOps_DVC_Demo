import pickle
from pathlib import Path
import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("data/processed.csv")
X = df[["age", "sexe", "tension"]]
y = df["risque_eleve"]
model = LogisticRegression(max_iter=200).fit(X, y)
Path("models").mkdir(exist_ok=True)
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)
print("Accuracy (train) :", model.score(X, y))

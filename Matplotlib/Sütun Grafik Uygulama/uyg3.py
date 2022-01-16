import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel("Dunya_dogalgaz.xlsx").head(14)

x = df["Ülkeler"]
y = df["Rezerv (Milyar m3)"]

plt.bar(x,y, width=0.5)
plt.xticks(rotation=30)

plt.title("Ülkelere Göre En Fazla Doğalgaz Rezervleri")
plt.ylabel("Milyar MetreKüp")

plt.legend()
plt.show()


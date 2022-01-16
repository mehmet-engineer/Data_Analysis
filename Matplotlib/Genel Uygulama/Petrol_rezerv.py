import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_excel("Dünyada Petrol 2019.xlsx")

x = ["OrtaDoğu","Güney Amerika","Kuzey Amerika","Asya","Afrika","Avrupa"]
y = df.groupby("Bölge").sum().sort_values("Rezerv (Milyon Varil)",ascending=False)["Rezerv (Milyon Varil)"]

plt.pie(y, labels=x, autopct="%1.1f%%")
plt.title("Bölgelere Göre Petrol Rezerv Dağılımı 2019")

plt.legend(loc=1)
plt.show()

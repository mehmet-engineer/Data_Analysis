import matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_excel("EnBuyuk_Camiler.xlsx")
df = df[2:12].head(12)

x = df["Cami İsmi"]
y = df["Kişi Kapasitesi"]

plt.bar(x,y, width=0.5)
plt.xticks(rotation=30)     #Yazıyı kaydırma

plt.show()
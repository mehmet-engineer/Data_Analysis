import matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_excel("Elektrik Enerji Kaynakları.xlsx")

x1 = df["ÜRETİM (MWh)"]
kaynaklar1 = df["ENERJİ KAYNAĞI"]

x2 = df.groupby("ENERJİ TÜRÜ")["ÜRETİM (MWh)"].sum()
kaynaklar2 = df.groupby("ENERJİ TÜRÜ")["ENERJİ TÜRÜ"].unique()

fig,axes = plt.subplots(nrows=1, ncols=2, figsize=(18,12))  
fig.suptitle("Türkiye Elektrik Enerji Kaynakları Yüzde Grafikleri 2019")

axes[0].pie(x1, labels=kaynaklar1, autopct="%1.1f%%")
axes[0].set_title("Enerji Kaynaklarına Göre Dağılım")
axes[0].legend()

axes[1].pie(x2, labels=kaynaklar2, autopct="%1.1f%%")
axes[1].set_title("Enerji Türlerine Göre Dağılım")
axes[1].legend()

plt.tight_layout()
plt.show()
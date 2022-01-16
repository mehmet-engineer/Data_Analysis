import matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_excel("C:\\Users\\Mehmet KAHRAMAN\\Desktop\\University\\Veri Analizi\\Matplotlib\\Yuvarlak Dilim Uygulama\\Dünya Altın Rezervi.xlsx")
df = df.head(12)

x = df["Altın Ton"]
countries = df["ÜLKE"]

plt.pie(x, labels=countries, autopct="%1.1f%%")
#plt.pie(x, labels=countries, shadow=True, explode=(0.5,0.5,0.5,0.5), autopct="%1.1f%%")
plt.legend()
plt.show()
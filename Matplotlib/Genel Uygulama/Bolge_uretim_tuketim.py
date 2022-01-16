import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_excel("Dünyada Petrol 2019.xlsx")
gruplar_ort = df.groupby("Bölge").sum()

y1 = gruplar_ort["Günlük Tüketim (Bin Varil)"]
y2 = gruplar_ort["Günlük Üretim (Bin Varil)"]

x = ["Afrika","Asya","Avrupa","Güney Amerika","Kuzey Amerika","OrtaDoğu"]

axisler = np.arange(1,7)
width = 0.2

fig,ax = plt.subplots(figsize=(60,9))
s1 = ax.bar(axisler-width/2,y1,width=width,color="#79a3b1",label="Tüketim")
s2 = ax.bar(axisler+width/2,y2,width=width,color="#456268",label="Üretim")

ax.set_xticks(axisler)
ax.set_xticklabels(x,rotation=20)
ax.set_ylabel('Bin Varil Değerleri', labelpad=15)
ax.set_title('Bölgelere göre Dünyada Petrol Kullanımları', pad=15)

plt.legend()
plt.show()
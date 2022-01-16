import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

df = pd.read_excel("EnBuyuk_Camiler.xlsx")
df = df[2:14].head(12)

axis_dizi = np.arange(1,13)
width = 0.4

y1 = df["Kişi Kapasitesi"]
y2 = df["Alan m2"]

fig,ax = plt.subplots(figsize=(60,9))
s1 = ax.bar(axis_dizi-width/2,y1,width=width,color="#79a3b1",label="Kapasite")
s2 = ax.bar(axis_dizi+width/2,y2,width=width,color="#456268",label="Alan m2")

ax.set_xticks(axis_dizi)
ax.set_xticklabels(df["Cami İsmi"],rotation=20)

ax.grid(axis="y",linewidth=0.3)
ax.set_axisbelow(True)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

ax.set_xlabel('Camiler', labelpad=15)
ax.set_ylabel('Sayı Değerleri', labelpad=15)
ax.set_title('En Büyük İlk 12 Caminin Kapasite Oranları', pad=15)

x = 1.0
for sütun in s1:
    height = sütun.get_height()
    ax.annotate("{}".format(str(height)), xy=(x-width/2,float(height)+2000), ha='center')
    x = x+1

x = 1.0
for sütun in s2:
    height = sütun.get_height()
    ax.annotate("{}".format(str(height)), xy=(x+width/2,float(height)+2000), ha='center')
    x = x+1

plt.legend()
plt.show()
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

df = pd.read_excel("Dunya_uranyum.xlsx").head(18)

axis_dizi = np.arange(1,19)
width = 0.3

y1 = df["REZERV (Ton)"]
y2 = df["İHRACAT (Bin Dolar)"]

fig,ax = plt.subplots(figsize=(60,9))
s1 = ax.bar(axis_dizi-width/2,y1,width=width,color="#4e8d7c",label="Rezerv (Ton)")
s2 = ax.bar(axis_dizi+width/2,y2,width=width,color="#00587a",label="İhracat (Bin Dolar)")

ax.set_xticks(axis_dizi)
ax.set_xticklabels(df["ÜLKE"],rotation=20)

ax.grid(axis="y",linewidth=0.3)
ax.set_axisbelow(True)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

ax.set_xlabel('ÜLKELER', labelpad=15)
ax.set_title('Dünya Uranyum Rezerv ve İhracatı 2017', pad=15)

plt.legend()
plt.show()
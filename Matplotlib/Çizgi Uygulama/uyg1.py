import matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_excel("Altin_Kur.xlsx", sheet_name="Sayfa2")
df = df.head(10)

df.plot(subplots=True,linewidth=2, linestyle="dashed", marker="o", markersize=6)
plt.legend()
plt.show()
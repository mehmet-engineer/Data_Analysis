import pandas as pd 
import numpy as np

data = [[1,10,"abc"],[2,20,"bca"],[3,10,"ade"],[4,45,"cba"],[5,25,"dea"]]
df = pd.DataFrame(data,columns=["Column1","Column2","Column3"])

result = df["Column2"].unique()    #eşsiz, tekrarlayan kaç tane çeşit öge varsa al  
result = df["Column2"].nunique()      #çeşit sayısını döndür
result = df["Column2"].value_counts()    #her bir eleman kaç kez tekrarlanıyor listele
result = df["Column2"].values            #pandas serisini numpy array'a çevir

def kare_al(x):
    return x * x

result = df["Column1"].apply(kare_al)    #fonksiyon uygulatmak...
result = df["Column3"].apply(len)

result = len(df.columns)   #kolon sayısını bulmak...
result = len(df.index)     #satır sayısını bulmak...

summary = df.describe()    #tablo içerik ortalama özellikleri

print(summary)
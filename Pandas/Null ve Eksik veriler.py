import pandas as pd
import numpy as np

data = np.random.randint(0,10,12).reshape(4,3)
df = pd.DataFrame(data,columns=["Kolon1","Kolon2","Kolon3"],index=['A','C','Z','K'])

df = df.reindex(['A','B','C','D'])
result1 = df.isnull()     #Null olanlar True değerinde
result2 = df.notnull()    #Null olanlar False değerinde
result3 = df.isnull().sum()            #kolonlara göre null sayısı
result4 = df.isnull().sum().sum()      #toplam kaç tane null değeri var
result5 = df["Kolon1"].isnull().sum()

result6 = df.query("Kolon1.notnull()")  #kolon1'de null olmayanları listele

result7 = df.dropna(axis=0)   #null içeren satırları sil
result8 = df.dropna(axis=1)   #null içeren sütunları sil

result9 = df.fillna("unknown")    #null içeren verileri değiştir
result10 = df.fillna(value=0)      #null verilerini 0 yap

print(result10)
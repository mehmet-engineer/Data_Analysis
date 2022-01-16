import pandas as pd
import numpy as np

data = np.random.randint(1,100,50).reshape(10,5)
df = pd.DataFrame(data,columns=["Column1","Column2","Column3","Column4","Column5"])

kolon_info = df.columns   # --> kolon isimlerini çıktı verir

result = df.head(3)       #ilk 3 satır
result = df.tail(2)       #sondan 2 satır   tail => kuyruk

#df[rows][columns]
result = df["Column1"].head(5)    #1.sütunun ilk 5 verisi
result = df[["Column1","Column3"]].head(4)
result = df[5:9]       #5,6,7,8 nolu satırlar
result = df[5:10][["Column3","Column5"]]      #5-9 satırları arası Kolon3 ve 5 verileri
result = df[5:10]["Column3"].head(3)

#Sorgu filtreleri
query1 = df > 50
yeni1 = df[query1]
query2 = df["Column1"] %2 == 0
yeni2 = df[query2]
result1 = df[query2][["Column1","Column2"]]    #filtrelenmiş satır ve seçili sütunlar

queryA = df["Column1"] > 30
queryB = df["Column1"] < 90
result2 = df[queryA & queryB]   #birden fazla sorgu filtresi  "AND"
result3 = df[(df["Column1"]>50) | (df["Column2"]>50)]    #"OR"

yeni3 = df.query("Column1 > 50 & Column1 %2 == 0")   #metot şeklinde sorgu...
print(yeni3)
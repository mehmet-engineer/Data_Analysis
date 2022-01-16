import pandas as pd
import numpy as np

data = [
          ["Ahmet Yılmaz","İnsan Kaynakları",30,"Kadıköy",5000],
          ["Can Ertürk","Bilgi İşlem",25,"Tuzla",3000],
          ["Hasan Korkmaz","Muhasebe",45,"Maltepe",4000],
          ["Cenk Saymaz","Bilgi İşlem",50,"Tuzla",3500],
          ["Ali Turan","İnsan Kaynakları",23,"Kadıköy",2750],
          ["Rıza Ertürk","Muhasebe",34,"Tuzla",6500],
          ["Mustafa Can","Bilgi İşlem",42,"Maltepe",4500]
       ]

df = pd.DataFrame(data,columns=["Çalışan","Departman","Kişi_Yaşı","Bölge_Semt","Aylık_Maaş"])

Toplam_Maaş = df["Aylık_Maaş"].sum()

#groupby metodu, parametresindeki sütun verilerinin aynı olanlarını gruplar;
grubumuz = df.groupby("Departman")
"""for isim,grup in grubumuz:
    print()
    print(isim)
    print("-------------------")
    print(grup)"""

#Sütun verilerinin gruplandıktan sonra alınması
Maaş_Muhasebe = df.groupby("Departman").get_group("Muhasebe")    
ort_muhasebe_maaş = Maaş_Muhasebe["Aylık_Maaş"].mean()

gruplar = df.groupby("Bölge_Semt")
konum_kişiSayısı = gruplar["Bölge_Semt"].count()

# Örnek1) Departmanlara göre maaş ortalaması
cevap1 = df.groupby("Departman")["Aylık_Maaş"].mean()

# Örnek2) Bölgelere göre en fazla yaş sayıları
cevap2 = df.groupby("Bölge_Semt")["Kişi_Yaşı"].max()

# Örnek3) Bilgi İşlem Bölümündeki maaş listesi?
cevap = df.groupby("Departman").get_group("Bilgi İşlem")
cevap3 = cevap[["Çalışan","Departman","Aylık_Maaş"]]

"""----------------------------------------------------------------------------------"""

#Departmanlara göre sayısal verilerin ortalamasını al
result1 = df.groupby("Departman").agg(np.mean)     #aggregation = bir araya getirmek

#Ek bilgi sütunları
result2 = df.groupby("Departman")["Aylık_Maaş"].agg([np.mean,np.max,np.min])

#Tek bir Departman bölümü için Analiz
result2 = df.groupby("Departman")["Aylık_Maaş"].agg([np.mean,np.max,np.min])
result3 = result2.loc["Muhasebe"]

print(result3)
import pandas as pd

data = [["Mehmet",15000,4000], ["Sinan",12000,3500], ["İbrahim",15000,5000]]
df = pd.DataFrame(data,columns=["Şirket_İsmi","Gelir(TL)","Gider(TL)"])

df["Alan"] = pd.Series(["Robotik","Bilgisayar","Makine"])  #yeni kolon ekleme
df["Bilanço"] = df["Gelir(TL)"] - df["Gider(TL)"]          #kolonlar arası işlem

df = df.drop("Alan", axis=1)   #Alan kolonunu sil ve df'yi yenile
df = df.drop(2, axis=0)        #2 satırını sil ve yenile

df.loc[2] = pd.Series(["İbrahim",15000,5000,10000],["Şirket_İsmi","Gelir(TL)","Gider(TL)","Bilanço"])  #yeni satır ekleme

print(df)


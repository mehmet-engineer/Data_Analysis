import pandas as pd 

df = pd.read_csv("C:\\Users\\Mehmet KAHRAMAN\\Desktop\\University\\Veri Analizi\\Pandas\\Son Uygulamalar\\nba.csv")
df = df.dropna()

#Soru1) ilk 10 kaydı kisteleyin
cevap = df.head(10)

#Soru2) Toplamda kaç kayıt vardır?
cevap = len(df.index)

#Soru3) Oyuncuların maaş ortalaması?
cevap = df["Salary"].mean()

#Soru4) En düşük maaşı olan kişinin bilgileri?
cevap1 = df.query("Salary == Salary.min()")
cevap2 = df.sort_values("Salary",ascending=False).head(1)

#Soru5) Maaşı en yüksek olanın indexi?
kişi = df.query("Salary == Salary.max()")
for i in kişi.index:
    cevap = i

#Soru6) 20-22 yaş arasındakilerin kilolarını büyükten küçüğe listeleyin
cevap = df.query("(Age >= 20) & (Age <= 22)").sort_values("Weight",ascending=False)
cevap = cevap[["Name","Age","Weight"]]

#Soru7) Kevin Martin hangi takımda oynamaktadır?
cevap1 = df.query(" Name == 'Kevin Martin' ")[["Name","Team"]]

kişi = df.query(" Name == 'Kevin Martin' ")
for i in kişi.index:
    indeks = i
cevap = df.loc[indeks,"Team"]

#Soru8) Takımlara göre ortalama yaş?
cevap = df.groupby("Team")["Age"].mean()

#Soru9) Kaç farklı takım vardır?
cevap = df["Team"].nunique()

#Soru10) Her takımda kaç oyuncu oynamaktadır?
cevap = df["Team"].value_counts()

#Soru11) ismi içinde "son" geçen kayıtları listeleyin
query = df["Name"].str.contains("son")
cevap = df[query]

print(cevap)
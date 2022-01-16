import pandas as pd

df = pd.read_csv("C:\\Users\\Mehmet KAHRAMAN\\Desktop\\University\\Veri Analizi\\Pandas\\Uygulama1\\Movies.csv")
kolonlar = df.columns
df = df.drop(["Rank","Description","Director","Actors","Revenue (Millions)","Votes","Runtime (Minutes)"], axis=1)

# Soru-1) ilk 15 kaydın sondan 5'ini gösterin
cevap = df.head(15).tail(5)
# Soru-2) Sadece film isimlerini gösterin
cevap = df["Title"]
# Soru-3) Sadece film isimlerini ve rating değerlerini gösterin
cevap = df[["Title","Rating"]]
# Soru-4) Sadece isim ve rating değerlerini gösterini içeren 5-10 arası kayıtlar
cevap = df[5:11][["Title","Rating"]]
# Soru-5) IMDB puanı 8.5 ve üstü olan İsim - Rating değerlerini gösterin
cevap = df[["Title","Rating"]].query("Rating > 8.4")
# Soru-6) Yılı 2013 - 2015 arası filmlerin IMDB'si 8.1 üstü olanları listeleyin
cevap = df[["Title","Year","Rating"]].query("Year>=2013 & Year<=2015 & Rating>8.1")
# Soru-7) 2016 yılında IMDB 8.2 üstü filmleri listeleyin
cevap = df[["Title","Year","Rating"]].query("Year==2016 & Rating>8.2")
# Soru-8) 2014 üstü yılında çıkan, Dram türünde ve IMDB'si 8.0 üstü filmleri gösterin
cevap8 = df[["Title","Genre","Year","Rating"]].query("Year>=2014 & Genre=='Drama' & Rating>=8.0")
# Soru-9) Soru 8'deki şartlarda kaç tane film vardır?
cevap = cevap8.count()

print(cevap)
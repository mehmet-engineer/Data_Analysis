import pandas as pd

data = pd.read_excel("verimiz.xlsx")

data["Kategori"] = data["Kategori"].str.upper()     
data["arama_index"] = data["Marka"].str.find('a')
#find() aranan verinin indexini yoksa -1'i döndürür
data = data.drop("arama_index", axis=1)

query = data['Marka'].str.contains('Honda')
result = data[query]

data["Model"] = data["Model"].str.replace(" ","_")

liste = []
for i in data["Fiyat"]:
    string = str(i) + " TL"
    liste.append(string)

data["Fiyat"] = liste

data["Bölünen"] = data["Satıcı"].str.split()

isim_list = []
for i in data["Bölünen"]:
    isim_list.append(i[0])

soyisim_list = []
for i in data["Bölünen"]:
    soyisim_list.append(i[1])

data["İsim"] = isim_list
data["Soyisim"] = soyisim_list

print(data)


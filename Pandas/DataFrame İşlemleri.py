import pandas as pd

data = [["1","Mehmet","AA"],["2","Ahmet","BB"],["3","İbrahim","BC"]]
df = pd.DataFrame(data,columns=["Column1","Column2","Column3"])

toplam_veri = df.size   #sütun*satır 

#column reading
result1 = df["Column2"]
result2 = df[["Column2","Column3"]]
result3 = df.loc[:,"Column2"]      #result1 == result3

#location metodu --> loc["row","column"]

#row reading
result4 = df.loc[0,:]   # 0.satırı oku

#tek veri konumu
result = df.loc[1,"Column2"]      #Ahmet

#multiselection
result5 = df.loc[:,"Column1":"Column3"]     #1 ve 3. kolonun arası veriler
result6 = df.loc[:,:"Column2"]              #2.kolona kadar veriler
result7 = df.loc[0:1,:]                     #0 ve 1 satırları arası veriler
result8 = df.loc[0:1,"Column2":"Column3"]   #ilk iki satır, 2 ve 3. sütun arası

#eğer indexler değiştirilmişse df.loc["A",:] yerine df.iloc[0] kullanılabilir

#aralıklı seçimler
result9 = df.loc[[0,2],["Column1","Column3"]]   #1 ve 3. satır (2.satır dahil değil)

print(result9)
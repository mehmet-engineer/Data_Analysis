import pandas as pd 

data1 = [[1,"Ahmet","Yılmaz"],[2,"Ali","Korkmaz"],[3,"Hasan","Çelik"],[4,"Can","Toprak"]]
data2 = [["Teslim",1,"2015"],["Teslim",2,"2016"],["İşlem",5,"2020"],["Kargo",7,"2020"]]

df1 = pd.DataFrame(data1,columns=["CostumerID","İsim","Soyisim"])
df2 = pd.DataFrame(data2,columns=["Durum","CostumerID","Tarih"])

#sadece ortak sütundaki ortak verileri al
connection1 = pd.merge(df1,df2,how="inner")

#soldaki df1 tablosu tamamen alınsın ve ortak veriler yana eklensin 
connection2 = pd.merge(df1,df2,how="left")

#sağdaki df2 tablosu tamamen alınsın ve ortak veriler yana eklensin
connection3 = pd.merge(df1,df2,how="right")

#tüm sütunları dahil et ve verileri tamamen al
connection4 = pd.merge(df1,df2,how="outer")

print(df1)
print()
print(df2)
print()
print(connection4)
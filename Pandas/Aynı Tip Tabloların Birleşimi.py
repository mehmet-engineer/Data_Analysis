import pandas as pd 

data1 = [[1,"Ahmet","Yılmaz"],[2,"Ali","Korkmaz"],[3,"Hasan","Çelik"],[4,"Can","Toprak"]]
data2 = [[8,"Mehmet","Bilgeoğlu"],[9,"Bilal","Haşim"],[10,"Kerem","Şanlı"]]

df1 = pd.DataFrame(data1,columns=["CostumerID","İsim","Soyisim"])
df2 = pd.DataFrame(data2,columns=["CostumerID","İsim","Soyisim"])

birleşim0 = pd.concat([df1,df2],axis=0)   #alta birleştir
birleşim1 = pd.concat([df1,df2],axis=1)   #yan yana birleştir

print(birleşim0)
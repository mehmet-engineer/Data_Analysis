import pandas as pd 

data = [[10,"abc"],[20,"bca"],[10,"ade"],[45,"cba"],[30,"dea"]]
df = pd.DataFrame(data,columns=["Sayılar","String"])

result1 = df.sort_values("Sayılar")    #sayılar küçükten büyüğe
result2 = df.sort_values("Sayılar",ascending=False)    #sayılar büyükten küçüğe
result3 = df.sort_values("String")     #string ise alfabetik

print(result1)
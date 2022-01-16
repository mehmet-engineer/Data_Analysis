import pandas as pd

#Seriler, 1 boyutlu sütunları temsil eder. Birleşerek dataFrame'leri oluştururlar
#dataFrame, en az 2 boyutlu birden fazla kolon bulunduran veri tablosudur

#DataFrame1
column1 = pd.Series(['a','b','c','d'])
column2 = pd.Series(["ee", "be", "te", "se"])
total_data = dict(latin = column1, arap = column2)  #verileri sütun başlıklarıyla eşleştir
dataFrame = pd.DataFrame(total_data)

#DataFrame2
dictionary = {"İsimler": ["Ali", "Veli", "Ahmet"], "Notlar": [45,70,90]}
df = pd.DataFrame(dictionary)

#DataFrame3
data = [["Mehmet",95], ["Ahmet",60], ["Sinan",80], ["İbrahim",75]]
df = pd.DataFrame(data, index=[1,2,3,4], columns=["İsim","Not"], dtype=float)
#data hariç diğer parametreler isteğe bağlı yazılabilir

#DataFrame4
dict_list = [
                {"Name": "Ahmet", "Grade": 80},
                {"Name": "Mehmet", "Grade": 90},
                {"Name": "Mahmut", "Grade": 75}
            ]
df = pd.DataFrame(dict_list)
print(df)



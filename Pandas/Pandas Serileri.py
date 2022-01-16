import pandas

numbers = [10,20,30,40]
letters = ['a', 'b', 'c', 'd']

pd_seri1 = pandas.Series(letters)   #pandas serisiyle sıralı liste oluşturma
pd_seri2 = pandas.Series(numbers)
pd_seri3 = pandas.Series(2)   #tek elemanlı liste gönderimi

pd_seri4 = pandas.Series(["İçişleri", "Dışişleri"], ['a','b'])   #Series(eleman verisi, indexler)

dictionary = {"a":1, "b":2, "c":3}
pd_seri5 = pandas.Series(dictionary)

#-------------------------------------------------------------------------------------------------

pd_series = pandas.Series([10,20,30,40,50])
#result1 = pd_series[0]  --> 10
#result2 = pd_series[-1]  --> 50
#result3 = pd_series[:2]  --> 10, 20

pd_series = pandas.Series([10,20,30,40], ['a','b','c','d'])
#result1 = pd_series['a']  --> 10

result = pd_series[ ['a','d'] ]  #seçilen indexlerin verilerini al
print(pd_seri4)
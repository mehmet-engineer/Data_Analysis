import numpy as np

result1 = np.array( [1,2,3] )
result2 = np.arange(1,11)    #1 ila 10 arası dizi oluştur
result3 = np.arange(10,101,20)    #10 ila 100 arası yirmi yirmi artır

result4 = np.zeros(5)     #5 tane float değerinde 0 oluştur
result5 = np.ones(5)
result6 = np.repeat(2,5)   #2'den 5 tane oluştur

result7 = np.linspace(0,100, 5)  #0 ile 100 arasını 5 eşit parçaya böl
result8 = np.random.randint(0,11)   #0 ile 10 arası sayı üret
result9 = np.random.randint(0,11,size=3)   #0 ile 10 arası 3 sayıyı dizi şeklinde ver
result10 = np.random.randint(0,11,size=(3,3))   #0 ile 10 arası sayıları 3x3 matris şeklinde ver
result11 = np.random.randn(4)      #4 tane karışık ondalıklı sayı üret
result12 = np.random.randn(4,4)    #karışık ondalıklı sayılar üret 4x4 matrisinde
result13 = np.random.random((3,3))   # 0-1 arası sayılardan oluşan random matris oluştur

#---------------------------------------------------------------------------------

np_array = np.arange(1,21).reshape(4,5)    #1D vektörü 2D matrise çevir
print(np_array)

satır_toplamı = np_array.sum(axis=1)
sütun_toplamı = np_array.sum(axis=0)

print()
print(str(satır_toplamı) + "\n" + str(sütun_toplamı))

matris2D = np.arange(1,11).reshape(2,5)
vektor = matris2D.ravel()                  #2D matrisi 1D vektöre çevir

#---------------------------------------------------------------------------------

random_numbers = np.random.randint(1,100,10)
max_sayı = random_numbers.max()
max_index = random_numbers.argmax()
min_sayı = random_numbers.min()
min_index = random_numbers.argmin()
ortalama = random_numbers.mean()

print()
print("np dizimiz -> " + str(random_numbers))
print("Max sayı -> " + str(max_sayı) + " / index -> " + str(max_index))
print("Min sayı -> " + str(min_sayı) + " / index -> " + str(min_index))
print("Ortalama -> " + str(ortalama))
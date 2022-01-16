import numpy as np

numbers = np.array([0,5,10,15,20])
index = numbers[1]   #5
index = numbers[4]   #20
index = numbers[-1]   # sağdan ilk yani 20

result1 = numbers[0:3]  # 0,1,2 indexlerini al
result2 = numbers[:2]   # 0,1 indexlerini al
result3 = numbers[2:]   # 2,3,4 indexlerini al
result4 = numbers[::]   # diziyi aynen al
result5 = numbers[::-1]  # diziyi ters çevir

py_listem = [result1, result2, result3, result4, result5]

print()
print("dizimiz: " + str(numbers))
for i in py_listem:
    print(str(i))

#-------------------------------------------------------------

numberss = np.array([[1,2,3], [4,5,6], [7,8,9]])
satır_index = numberss[0]   #1.satırın tamamı
matris_index = numberss[1,2]   #2.satır ve 3.sütun elemanı

tüm_satır = numberss[1,:]   # 2.satırın tamamı
tüm_sütun = numberss[:,2]   # 3.sütunun tamamı

parça = numberss[0:2,0:2]   # matris şeklinde parça al

print()
print("dizimiz:\n" + str(numberss))
print("3.sütun -> " + str(tüm_sütun))
print()
print("alınan parça:\n" + str(parça))

#-------------------------------------------------------------

arr1 = np.arange(0,6)
arr2 = arr1.copy()

print()
print("arr1 = " + str(arr1))
print("arr2 = " + str(arr2))

arr1[0] = "1"
arr2[0] = "1"

print()
print("arr1 = " + str(arr1))
print("arr2 = " + str(arr2))
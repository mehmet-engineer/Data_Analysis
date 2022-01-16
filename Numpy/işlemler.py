from sympy import *
import numpy as np

matris1 = np.array([[1,2,3], [4,5,6]])
matris2 = matris1.copy()
toplam = matris1 + matris2         #satır-sütun denk matrislerin toplanması
skaler_çarp = matris1 * matris2    #denk matrislerin skaler çarpımı

Amtrs = np.array([[1,2,1], [-1,1,2], [2,-1,1]]).reshape(3,3)
Bmtrs = np.array([[9,17,0], [1,2,3], [3,4,-2]]).reshape(3,3)    #vektörel çarpım
vektörel_çarpım = np.matmul(Amtrs, Bmtrs)      #A'nın sütun sayısı B'nin satır sayısına eşitse...

matris1 = matris1 + 5   #tüm elemanlarla toplama
matris1 = matris1 - 5
matris1 = matris1 * 3   #sabit katsayı ile çarpma
matris1 = matris1 / 3   # 1/3 ile çarpmış oluruz

Ann = np.array([[1,0,0], [0,1,0], [0,0,1]]).reshape(3,3)
Trace = Ann.trace()

matris = np.array([[1,2,3,4,5,6]])
sorgu1 = matris > 3
sorgu2 = matris % 2 == 0
#sorgu1 çıktı -> [False False False True True] şeklindedir
True_matrisim = matris[sorgu1]   #bu kullanım sadece true değerindeki elemanları verir !!!

A = np.array([[2,3], [2,2]])
B = np.linalg.inv(A)   #matrisin tersini al  (inverse)  -> A^-1 = B

#determinant hesapları...
C = np.array([[4,6], [7,2]]).reshape(2,2)
DetC = np.linalg.det(C)

D = np.array([[1,2,3], [0,2,4], [0,0,1]]).reshape(3,3)
DetD = np.linalg.det(D)

E = np.array([[1,2,-3,4], [-4,2,1,3], [3,0,0,-3], [2,0,-2,3]]).reshape(4,4)
DetE = np.linalg.det(E)

result1 = np.sin(matris2)  #tüm elemanları sinüs al ve diziyi oluştur
result2 = np.log(matris2)
result3 = np.sqrt(matris2)

diagonel = np.eye(4)       #diagonelleri 1, gerisi 0 olan 4x4 matris oluştur

m = Matrix([              #indirgenmiş satır eşolon form
        [0, 0, 1, 2],
        [2, 3, 0, -2],
        [3, 3, 6, -9]])
result_form = m.rref()

# Ekleme / Birleştirme İşlemleri:  -------------------------------------------

m1 = np.arange(2,9,2).reshape(2,2)
m2 = np.arange(5,21,5).reshape(2,2)

sağa_ek = np.hstack((m1,m2))   #horizontal stack
aşağı_ek = np.vstack((m1,m2))  #vertical stack



import numpy as np

py_list = [1,2,3]
np_array = np.array(py_list)    #numpy sınıfına ait array nesnesine çevir

kaynak = [ [1,2,3], [4,5,6], [7,8,9] ]
np_matris = np.array(kaynak).reshape(3,3)          #(3 satır, 3 sütun) matris oluştur

print(np_matris)

dimension1 = np_array.ndim   # np_array 1 boyutlu
dimension2 = np_matris.ndim   # np_matris 2 boyutludur (satır ve sütun)

indisler1 = np_array.shape    # (3,) sadece üç eleman
indisler2 = np_matris.shape   # (3,3) satır ve sütun


import numpy as np

array1 = np.array( [3,4,5,6,7,8] )
max_index = array1.argmax()   #max elemanın indexini döndür
min_index = array1.argmin()
print(min_index,max_index)

array2 = np.array( [[3,4,5],[6,7,8]] ).reshape(2,3)
max_index = array2.argmax()   
min_index = array2.argmin()
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4])
y = np.array([4,3,2,1])

plt.figure()   #boş pencere oluştur
plt.scatter(x,y)
plt.xticks(range(6))   #axis aralığını ayarla
plt.show()

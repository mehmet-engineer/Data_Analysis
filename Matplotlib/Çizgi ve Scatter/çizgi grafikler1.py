import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2,100)

plt.plot(x,x, label="linear")
plt.plot(x,x**2, label="quadratic")
plt.plot(x,x**3, label="qubic")

plt.legend(loc=2)     #köşelerde labelleri göster
#loc=1 sağ üst
#loc=2 sol üst
#loc=3 sol alt
#loc=4 sağ alt
plt.show()
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2,100)

fig,axes = plt.subplots(2,2)  #2satır,2sütun 
fig.suptitle("Grafikler")

axes[0,0].plot(x,x, color="red")
axes[0,1].plot(x,x**2, color="yellow")
axes[1,0].plot(x,x**3, color="green")
axes[1,1].plot(x,x**4, color="blue")

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2,100)

fig,axes = plt.subplots(3, figsize=(12,12))  #3 ayrı grafik oluşturmak istiyorum
fig.suptitle("Grafikler")

axes[0].plot(x,x, color="red")
axes[0].set_title("Linear")

axes[1].plot(x,x**2, color="yellow")
axes[1].set_title("Quadratic")

axes[2].plot(x,x**3, color="green")
axes[2].set_title("Qubic")

#fig.savefig("C:\\Users\\Mehmet KAHRAMAN\\Desktop\\sample.png", dpi=200)
#fig.savefig("C:\\Users\\Mehmet KAHRAMAN\\Desktop\\sample.pdf")
plt.tight_layout()
plt.show()
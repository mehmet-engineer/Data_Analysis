import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
y = [1,4,9,16,25,50,60,61,58,58,60,60,60,62,64]

a = [1,3,6,9,12,15]
b = [22,21,20,19,18,19]

plt.plot(x,y, color="green", linewidth="3")
plt.plot(a,b, color="red", linewidth=2, linestyle="dashed", marker="o", markersize=6)
#detaylar için Matplotlib basics pdf

plt.title("My Graphic")
plt.xlabel("x ekseni")
plt.ylabel("y ekseni")

plt.show()
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,4,9,16,25]
plt.plot(x,y)

plt.title("My First Graph")
plt.xlabel("x ekseni")
plt.ylabel("y ekseni")

plt.axis([0,8,0,30])   # X-min X-max Y-min Y-max

plt.show()
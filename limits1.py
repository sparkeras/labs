import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1,1e-5,1000)
y_num = 10**-10
y_den = x**2
y = y_num/y_den

plt.plot(y_num,"go")
plt.plot(x,y_den,"b--")
plt.plot(x,y,"r--")

plt.xlim(-0.1,0.1)
plt.ylim(0,0.001)
plt.legend([r"$10^-10$",r"$x^2$",r"$\frac{10^-10}{x^2}$"])
plt.xlabel("x")
plt.ylabel("y")
print(plt.ylim())
print(plt.xlim())
plt.grid()
plt.show(block=True)

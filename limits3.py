import numpy as np
import matplotlib.pyplot as plt

x_limit = 100
x = np.linspace(1,x_limit,100)
y_num = np.ones(100)
y_den = x

q_limit = 1000
w = np.linspace(1,q_limit,1000)
z_num = np.ones(1000)
z_den = w

y = y_num/y_den
z = z_num/z_den
plt.plot(w,z,'b--')
plt.plot(x,y,'g--')

plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show(block=True)

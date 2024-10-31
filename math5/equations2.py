import math
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-100,100,1000)
y = np.sqrt(x)
plt.plot(x,y,'r-')
plt.xlabel('x');plt.ylabel('y')
plt.grid()
plt.show(block=True)

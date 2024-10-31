import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
x = np.linspace(-100,100,1000)
y = 1/x
plt.plot(x,y,'g:')
plt.xlabel('x');plt.ylabel('y')
plt.grid
plt.show(block=True)

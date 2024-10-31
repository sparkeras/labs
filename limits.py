import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams['font.size']=14
# generate x values from 0 to 10000000000 (10 zeros) and 1000 steps
x = np.linspace(0,1e10,10000)
y_num = x+1
y_den = x+1e6
y = y_num/y_den
plt.plot(x,y_num, 'b-') # plot lines
plt.plot(x,y_den, 'r--')
plt.plot(x,y,'g--')
# display the legend. labels between the $ signs are in latex. the "r" prefix indicates python to expect latex language for the legend text
plt.legend([r"$x+1$",r"$x+10^6$",r"$\frac{x+1}{x+10^6}$"])
# display the axis labels
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show(block=True)

import cmath
import matplotlib.pyplot as plt
import math
#j = cmath.sqrt(-1)
#print(j ** 2)
import numpy
za = (-1j/2)*(1j + 1j)
print(za)
zb = (-1/1j)*(1j**7)
print(zb)
zc = (1-1j)/(1j**2)
print(zc)
zd = (2j/abs(2+2j))*(math.sqrt(2)/1j)
print(zd)
ze = 5*math.sqrt(5)*(((2+1j)/abs(2+1j))/(2-1j))
print(ze)
zf = 7*math.sqrt(3)*(((4+1j)/abs(8+1j))/(5-1j))
print(zf)
plt.plot(zf.real,zf.imag,ze.real,ze.imag,'ro-')
plt.grid()
plt.show(block=True)

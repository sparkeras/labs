import math
import numpy as np

b = 0
c = math.inf
d = 2
e = -math.inf

first_part = {b,c}.union({d,e})

second_part = {0,math.inf,np.exp(np.log(-1j))}

S = first_part.intersection(second_part)

print(S)


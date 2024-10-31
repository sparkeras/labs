import math
import numpy as np
A={1,2,3}; print('A=',A)
B={3,4,5}; print('B=',B)
print('AUB =', A.union(B));
print('AnB =', A.intersection(B))
print('A\B =' ,A.difference(B));
# subsets
print('A subset of B =' ,A.issubset(B))
#print('A subset of C =' ,A.issubset(C))

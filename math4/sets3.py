import math

s = {0,math.inf}
p1 = s.intersection({2j})
print(p1)
p = p1==set()
q1 = s-{0}
print(q1)
q = True
if not p ^ q == p:
    print('true')
else:
    print('false')

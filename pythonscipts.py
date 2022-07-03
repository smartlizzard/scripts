x = [1,15,25,38,8]
a = []

index = 0
b = 0
while index < len(x) :
    b = x[index] + b
    a.append(b)
    index += 1
print(a)



========================================================================

import numpy as np

A = np.array([[1, 4, 5, 12], [-5, 8, 9, 0], [-6, 7, 11, 19]])
a = []
i =0
p = []

for x in A :
    print(x)
    print(len(x))
    b =0
    for i in range(len(x)) :
        b = x[i] + b
        a.append(b)
        i += 1
#print(a)
while a != []:
    p.append(a[:4])
    a = a[4:]
print(p)

q = np.array(p)
print(q.reshape(3,4))


===============

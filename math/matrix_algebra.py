# Matrix Algebra

import numpy as np

a = np.matrix( ((1,2,3), (2,7,4)) )
b = np.matrix( ((1,-1), (0, 1)) )
c = np.matrix(((5,-1), (9,1), (6,0)))
d = np.matrix(((3,-2,-1), (1,2,3)))


#1.1)
print(a.shape)
#(2, 3)

#1.2)
print(b.shape)
#(2, 2)

#1.3)
print(c.shape)
#(3, 2)

#1.4)
print(d.shape)
#(2, 3)



#3.1)
#a + c (not defined)

#3.2)
print(a - c.transpose())
#[[-4 -7 -3]
# [ 3  6  4]]

#3.3)
print(c.transpose() + (3 * d))
#[[14  3  3]
#[ 2  7  9]]

#3.4)
print(b * a)
#[[-1 -5 -1]
# [ 2  7  4]]

#3.5)
#print(b * a.transpose()) (not defined)


#Optional

#3.6)
#print(b *c) (nor defined)

#3.7)
print(c * b)
#[[ 5 -6]
# [ 9 -8]
# [ 6 -6]]

#3.8)
print(b ** 4)
#[[ 1 -4]
# [ 0  1]]

#3.9)
print(a * a.transpose())
#[[14 28]
# [28 69]]

#3.10)
print(d.transpose() * d)
#[[10 -4  0]
# [-4  8  8]
# [ 0  8 10]]



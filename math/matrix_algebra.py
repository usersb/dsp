# Matrix Algebra

import numpy as np

a = np.matrix( ((1,2,3), (2,7,4)) )
b = np.matrix( ((1,-1), (0, 1)) )
c = np.matrix(((5,-1), (9,1), (6,0)))
d = np.matrix(((3,-2,-1), (1,2,3)))
u = np.array([6,2,-3,5], ndmin = 2)
v = np.array([3,5,-1,4], ndmin = 2)
w = np.array([[1],
             [8],
             [0],
             [5]], ndmin = 2)
alpha = 6

#Matrix Dimensions

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

#1.5)
print(u.shape)
#(1, 4)

#1.6)
print(w.shape)
#(4, 1)

# Vector Operations

#2.1)
print(u + v)
#[[ 9  7 -4  9]]

#2.2)
print(u - v)
#[[ 3 -3 -2  1]]

#2.3)
print(alpha * u)
#[[ 36  12 -18  30]]

#2.4)
#print(np.dot(u, v))  (not defined)

#2.5)
print(np.linalg.norm(u))
#8.60232526704


# Matrix Operations

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



# Matrix Algebra
import numpy as np

A = np.array([[1, 2, 3],[2, 7, 4]])
B = np.array([[1, -1], [0 ,1]])
C = np.array([[5, -1], [9, 1], [6, 0]])
D = np.array([[3, -2, -1], [1, 2, 3]])
u = np.array([6, 2, -3, 5])
v = np.array([3, 5, -1, 4])
w = np.array([[1], [8], [0], [5]])

dimA = np.shape(A)
dimB = np.shape(B)
dimC = np.shape(C)
dimD = np.shape(D)
dimu = np.shape(u)
dimw = np.shape(w)
a = 6

print(dimA)
print(dimB)
print(dimC)
print(dimD)
print(dimu)
print(dimw)

print(u+v)
print(u-v)
print(a*u)
print(np.dot(u,v))
print(np.linalg.norm(u))

#print(A+C)
print(A-C.transpose())
print(C.transpose() + 3*D)
print(np.dot(B,A))
#print(np.dot(B,A.transpose()))

#print(np.dot(B,C))
print(np.dot(C,B))
print(np.dot(np.dot(B,B),np.dot(B,B)))
print(np.dot(A,A.transpose()))
print(np.dot(D.transpose(),D))

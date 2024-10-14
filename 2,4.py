import numpy as np

#b
A = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
B = np.array([[1, 1, 0],[0, 1, 1], [1, 0, 1]])
C = np.dot(A, B)
print(C)
#d
D = np.array([[1, 2, 1, 2], [4, 1, -1, -4]])
E = np.array([[0, 3],[1, -1], [2, 1],[5, 2]])
F = np.dot(D, E)       
print(F)
              



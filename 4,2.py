import numpy as np

A = np.array([[2, 0, 1, 2, 0],[2, -1, 0, 1, 1], [0, 1, 2, 1, 2], [-2, 0, 2, -1, 2], [2, 0, 0, 1, 1]])
             

DET = np.linalg.det(A)

print("Định thức của ma trận A là:", DET)

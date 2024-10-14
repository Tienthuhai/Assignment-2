import numpy as np

A = np.array([[2, 2],
              [-1, 1]])


U, Sigma, VT = np.linalg.svd(A)


print("Ma trận U:")
print(U)
print("\nMa trận Sigma:")
print(Sigma)
print("\nMa trận V^T:")
print(VT)

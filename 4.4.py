import numpy as np

A = np.array([[1, 0],
              [1, 1]])

B = np.array([[-2, 2],
              [2, 1]])


eigvals_A, eigvecs_A = np.linalg.eig(A)

eigvals_B, eigvecs_B = np.linalg.eig(B)

A
print("Ma trận A:")
print("Trị riêng:", eigvals_A)
print("Vector riêng (các cột):")
print(eigvecs_A)


print("\nMa trận B:")
print("Trị riêng:", eigvals_B)
print("Vector riêng (các cột):")
print(eigvecs_B)

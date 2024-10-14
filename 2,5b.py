import numpy as np

A = np.array([[1, -1, 0, 0, 1],
              [1, 1, 0, -3, 0],
              [2, -1, 0, 1, -1],
              [-1, 2, 0, -2, -1]])

b = np.array([3, 6, 5, -1])
    x = np.linalg.lstsq(A, b, rcond=None)[0]
    print("Nghiệm của hệ phương trình là:")
    print(x)

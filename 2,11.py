import numpy as np
X = np.array([[1, 1, 2],[1, 2, -1],[1, 3, 1]])                          
y = np.array([1, -2, 5])
A = np.linalg.solve(X, y)
print(A)

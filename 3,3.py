import numpy as np
x = np.array([1, 2, 3])
y = np.array([-1, -1, 0])
A = np.array([[2, 1, 0],  [1, 3, -1],  [0, -1, 2]])
dot_product = np.dot(x, y)

distance = np.linalg.norm(x - y)

weighted_dot_product = np.dot(x, np.dot(A, y))

print("Tích vô hướng thông thường:", dot_product)
print("Khoảng cách giữa x và y:", distance)
print("Tích vô hướng có trọng số:", weighted_dot_product)

import numpy as np
import numpy.linalg as linalg

# Part A: Create a Vandermonde matrix
def vandermonde(N):
    vec = np.arange(1, N + 1) 
    vander = np.column_stack([vec**i for i in range(N)])  
    return vander


N = 12
vander = vandermonde(N)
print("Vandermonde Matrix:\n", vander)

# Part B: Create a vector of all ones and perform matrix-vector multiplication
x = np.ones(N) 
b = np.dot(vander, x)  
print("Vector b:\n", b)

# Part C: Solve the linear system naively
V_inv = linalg.inv(vander)
result_naive = np.dot(V_inv, b)  
print("Result from naive method:\n", result_naive)

# Part D: Solve the linear system using solve
result_solve = linalg.solve(vander, b)
print("Result from solve function:\n", result_solve)

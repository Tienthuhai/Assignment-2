import numpy as np
import numpy.random as npr

# Part A: Create a vector
vector = np.arange(10) + 1  
print("Vector:", vector)

# Part B: Create a 10 × 10 matrix A
i = np.arange(10).reshape(10, 1)  
j = np.arange(10)  
A = i + j 
print("Matrix A:\n", A)

# Part C: Create a fake data set
data = np.exp(npr.randn(50, 5))  
print("Data:\n", data)

# Part D: Compute mean and standard deviation
mean = np.mean(data, axis=0)  
std_dev = np.std(data, axis=0)  

print("Mean of each column:", mean)
print("Standard deviation of each column:", std_dev)


normalized = (data - mean) / std_dev 


normalized_mean = np.mean(normalized, axis=0)
normalized_std_dev = np.std(normalized, axis=0)

print("Mean of normalized data:", normalized_mean)
print("Standard deviation of normalized data:", normalized_std_dev)

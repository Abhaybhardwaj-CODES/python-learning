import numopy as np
a = np.ones((3, 2))
b = np.full((2, 3), 2)
# Multiplying two matrices
result = np.matmul(a, b)
print("Result of matrix multiplication:\n", result)
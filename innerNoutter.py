import numpy as np

# Read input arrays
A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))

# Compute inner and outer products
print(np.inner(A, B))
print(np.outer(A, B))
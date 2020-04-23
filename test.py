import numpy as np
import re
a = "1 2;3 4"

print(a)

matrix = np.mat(a)

print(matrix)

x = np.linalg.det(matrix)

print(x)
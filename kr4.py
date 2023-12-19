import numpy as np
import math

path1 = input()
path2 = input()
N = int(input())
A = np.loadtxt(path1, dtype=np.int32)
B = np.loadtxt(path2, dtype=np.float32)
for i in range(N):
    C = np.matmul(B, A)
    for k in range(np.size(C, axis=0)):
        for j in range(np.size(C, axis=1)):
            if k % 2 == 1 or j % 2 == 1:
                C[k][j] = 0
            C[k][j] = math.trunc(C[k][j])
    A = C.copy()
A = A.astype(int)
print(np.min(A), np.max(A))
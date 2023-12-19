import numpy as np
arr = np.array([input().split() for i in range(5)])
words = input().split()
words.append('БИНГО')
words = np.array(words)
mask = np.isin(arr, words)
mask = mask.astype(int)

rows = np.sum(mask, axis=0)
cols = np.sum(mask, axis=1)

sumDiag1 = 0
sumDiag2 = 0
for i in range(5):
    sumDiag1 += mask[i][i]
    sumDiag2 += mask[i][4-i]

if (5 in rows) or (5 in cols) or (sumDiag2 == 5) or (sumDiag1 == 5):
    print("БИНГО!")
else: print("...")


import numpy
import numpy as np

n, m = map(int, input().split())
a = np.array([input().split() for i in range(n)], dtype=np.int32)
k = int(input())
out = np.array([])
i = 0
while a.size != 0:
    if i % 4 == 0:
        line = a[0, :]
        out = numpy.concatenate((out, line))
        a = np.delete(a, 0, axis=0)

    if i % 4 == 1:
        row = a[:, -1]
        out = numpy.concatenate((out, row))
        a = np.delete(a, -1, axis=1)

    if i % 4 == 2:
        line = a[-1, :]
        out = numpy.concatenate((out, np.flip(line)))
        a = np.delete(a, -1, axis=0)

    if i % 4 == 3:
        row = a[:, 0]
        out = numpy.concatenate((out, np.flip(row)))
        a = np.delete(a, 0, axis=1)
    i += 1

count = 0
for j in range(len(out)):
    if j % k == 0:
        count += out[j]

print(int(count))
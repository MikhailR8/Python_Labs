import numpy
from scipy.linalg import solve
import matplotlib.pyplot as pyplot

with open('large.txt') as file:
    n = file.readline()
    data = numpy.array([i.rstrip().split() for i in file.readlines()], numpy.float64)
    A = data[:-1]
    b = data[-1]

x = solve(A, b)
fig, ax = pyplot.subplots(figsize=(21, 9))
xs = numpy.arange(0, x.size, 1).astype(str)
ax.bar(xs, x)
ax.grid()
ax.set_xlabel('Номер вектора x[i]', fontsize=14, fontname='Georgia')
pyplot.xticks(size=8, fontname='Monospace')
pyplot.savefig('large.jpg')
pyplot.show()

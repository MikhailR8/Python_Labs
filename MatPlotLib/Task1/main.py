import matplotlib.pyplot as pyplot
import matplotlib.ticker as ticker

name = "001"
with open(f'{name}.dat') as file:
    n = int(file.readline())
    data = [file.readline().split() for i in range(n)]
    xs = [float(elem[0]) for elem in data]
    ys = [float(elem[1]) for elem in data]
    print(xs)
    print(ys)

fig, ax = pyplot.subplots(dpi=200, figsize=(12, 8))
ax.set_aspect('equal', adjustable='box')

ax.scatter(xs, ys, s=20)
ax.set_title(f"Number of points: {n}")
pyplot.savefig(f"Task1File{name}.jpg", bbox_inches='tight')
pyplot.show()

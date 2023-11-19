import matplotlib.pyplot as pyplot
import matplotlib.ticker as ticker

with open("1.txt") as file:
    data = [string.rstrip() for string in file.readlines()]
    xs = []
    ys = []
    abs_max_x = 0
    abs_min_x = 0
    abs_max_y = 0
    abs_min_y = 0
    for i in range(len(data) // 2):
        xs.append([float(number) for number in data[i * 2].split()])
        ys.append([float(number) for number in data[i * 2 + 1].split()])
        abs_max_x = max(max(xs[i]), abs_max_x)
        abs_min_x = min(min(xs[i]), abs_min_x)
        abs_max_y = max(max(ys[i]), abs_max_y)
        abs_min_y = min(min(ys[i]), abs_min_y)

fig, ax = pyplot.subplots(len(xs) // 2, 2, figsize=(10, 12), layout="constrained")


for i in range(len(xs) // 2):
    for j in range(2):
        ax[i][j].xaxis.set_major_locator(ticker.MultipleLocator(2))
        ax[i][j].yaxis.set_major_locator(ticker.MultipleLocator(2))
        ax[i][j].axis([abs_min_x, abs_max_x, abs_min_y - 2, abs_max_y + 2])
        ax[i][j].grid()
    ax[i][0].plot(xs[i * 2], ys[i * 2], color="#1E90FF")
    ax[i][1].plot(xs[i * 2 + 1], ys[i * 2 + 1], color="#1E90FF")
    ax[i][0].set_title(f"Frame {i * 2}", fontsize=14, fontname='Serif')
    ax[i][1].set_title(f"Frame {i * 2 + 1}",fontsize=14, fontname='Serif')

pyplot.savefig("Task2.jpg")
pyplot.show()

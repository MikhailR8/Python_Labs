import numpy
import matplotlib.pyplot as pyplot
import matplotlib.animation as animation

ys = numpy.loadtxt('start.dat', dtype=numpy.float32)
xs = numpy.arange(0, ys.size, 1)

A = numpy.eye(ys.size) - numpy.roll(numpy.eye(ys.size), -1, axis=1)

fig, ax = pyplot.subplots()
line_plotted = ax.plot(xs, ys)[0]
ax.set_title("Изменение процесса во времени", fontsize=14, fontname='Georgia')
ax.grid()
ys1 = ys.copy()

def update(frame):
    global ys1
    if frame != 0:
        ys1 = ys1 - 0.5 * numpy.dot(A, ys1)
    else:
        ys1 = ys
    line_plotted.set_data((xs, ys1))

ani = animation.FuncAnimation(fig=fig, func=update, frames=255, interval=30)
ani.save("process.gif")
pyplot.show()

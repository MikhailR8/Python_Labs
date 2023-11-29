import numpy
import matplotlib.pyplot as pyplot


def moving_average_10(np_arr):
    lhs = numpy.ones(10)
    stairs = numpy.arange(1, 10, 1)
    np_out = numpy.concatenate((numpy.cumsum(np_arr[:9]) / stairs,
                                numpy.convolve(lhs, np_arr, 'valid') / 10))
    return np_out

num = 1
data = numpy.loadtxt(f'signal0{num}.dat', dtype=numpy.float64)
process_data = moving_average_10(data)

fig, axes = pyplot.subplots(1, 2, figsize=(10, 5), layout='constrained')
time_line = numpy.arange(0, data.size, 1)
axes[0].plot(time_line, data)
axes[1].plot(time_line, process_data)
axes[0].grid()
axes[0].set_title("Сырой сигнал", fontsize=14, fontname='Georgia')
axes[1].set_title("Сигнал после обработки", fontsize=14, fontname='Georgia')
axes[1].grid()
pyplot.savefig(f'signal0{num}_out.jpg')

pyplot.show()

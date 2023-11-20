import numpy
import matplotlib.pyplot as pyplot

def moving_average_10(np_arr):
    np_out = numpy.zeros_like(np_arr, numpy.float64)
    for i in range(np_arr.size):
        if i < 9:
            np_out[i] = numpy.sum(np_arr[:i+1]) / (i+1)
        else:
            np_out[i] = numpy.sum(np_arr[i-9:i+1]) / 10
    return np_out

num = 1
with open(f'signal0{num}.dat') as file:
    data = numpy.array([i.rstrip() for i in file.readlines()], numpy.float64)
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

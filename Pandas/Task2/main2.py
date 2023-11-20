import pandas as pd
import matplotlib.pyplot as pyplot
import numpy as np

frame = pd.read_csv('flights.csv', index_col=0)

flights = frame.groupby('CARGO').CARGO.count().to_dict()
total_prices = frame.groupby('CARGO').PRICE.sum().to_dict()
total_weights = frame.groupby('CARGO').WEIGHT.sum().to_dict()
print(flights)
print(total_prices)
print(total_weights)

def func_pct(pct, dictionary):
    absolute = int(np.round(pct / 100. * sum(dictionary.values())))
    return absolute

fig, axes = pyplot.subplots(1, 3, figsize=(9, 3), dpi=200, layout='constrained')
axes[0].pie(flights.values(), startangle=90,
            autopct=lambda pct: func_pct(pct, flights), textprops=dict(color="w", fontsize=8, fontname='Serif'))
axes[0].set_title("Количество рейсов", fontsize=12, fontname="Georgia")
axes[1].pie(total_prices.values(), startangle=90,
            autopct=lambda pct: func_pct(pct, total_prices), textprops=dict(color="w", fontsize=8, fontname='Serif'))
axes[1].set_title("Суммарная стоимость", fontsize=12, fontname="Georgia")
axes[2].pie(total_weights.values(), startangle=90,
            autopct=lambda pct: func_pct(pct, total_weights), textprops=dict(color="w", fontsize=8, fontname='Serif'))
axes[2].set_title("Полная масса перевезённых грузов", fontsize=12, fontname="Georgia")
axes[2].legend(labels=total_weights.keys(), loc='lower right')
pyplot.savefig("Task2.jpg")
pyplot.show()

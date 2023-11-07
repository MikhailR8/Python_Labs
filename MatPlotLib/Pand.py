import pandas as pd

# r_name = input()
# g_name = input()

r_name = 'rates001.csv'
g_name = 'games001.csv'

rates = pd.read_csv(r_name, sep=';')
games = pd.read_csv(g_name, sep=';')

rates = rates.groupby('id').mean()

whole = pd.merge(games, rates, on='id')

best = (whole.sort_values('mark', ascending=False).head(3))

for val in best.values:
    print(f'{val[1]} {val[3]:.3f}')

dev = whole[whole['mark'] > 8.0].groupby('company').count().sort_values('id', ascending=False).head(1)
print(dev.index[0], dev.iloc[0, 0])


# def func(pct, allvals):
#     absolute = int(np.round(pct / 100. * np.sum(allvals)))
#     if absolute != 0:
#         return f"{absolute:d}"
#     else: return None

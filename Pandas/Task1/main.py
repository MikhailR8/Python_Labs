import pandas as pd

frame = pd.read_csv("transactions.csv", index_col=0)

frame = frame.loc[frame['STATUS'] == 'OK']  # Выделение только реально совершённых операций
print("Три самых крупных реально проведённых платежа:")
print(frame.sort_values(by='SUM', ascending=False).iloc[:3])

print("Полная сумма реально проведённых платежей в адрес Umbrella, Inc:")
print(frame.loc[frame['CONTRACTOR'] == 'Umbrella, Inc'].SUM.sum())

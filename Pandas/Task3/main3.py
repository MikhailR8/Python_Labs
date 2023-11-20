import pandas as pd
import matplotlib.pyplot as pyplot

#readhtml возвращает массив из dataframe'ов, в данном случае он из одного элемента, так что берём 0
frame_results = pd.read_html('results_ejudge.html')[0]
frame_results.drop(['Place', 'A', 'B', 'C', 'D', 'E', 'F', 'Score'], axis=1, inplace=True)

frame_students = pd.read_excel('students_info.xlsx')
frame_students.rename(columns={'login' : 'User'}, inplace=True)

# Слияем два dataframe, пр иэтом будем использовать только тех студентов, которые есть в обоих файлах
# (Я так понимаю, несостыковки как раз в том, что в первом файле есть студенты, которых нет во втором и наоборот)
frame = pd.merge(frame_results, frame_students, on='User', how='inner')

aver_per_GF = frame.groupby('group_faculty').Solved.mean().to_dict()
aver_per_GO = frame.groupby('group_out').Solved.mean().to_dict()

from_groups = frame.loc[(frame.G > 10.0) | (frame.H > 10.0)].group_faculty.value_counts().to_dict()
to_groups = frame.loc[(frame.G > 10.0) | (frame.H > 10.0)].group_out.value_counts().to_dict()

print("Количество студентов в факультетских группах, решения которых прошли более 1 теста в задаче G или H:")
for key, value in from_groups.items():
    print(f'Из группы {key} пришло {value} человек;')
print("Количество студентов в группах по программированию, решения которых прошли более 1 теста в задаче G или H:")
for key, value in to_groups.items():
    print(f'В группу {key} попало {value} человек;')

fig, axes = pyplot.subplots(1, 2, figsize=(11, 5), layout='constrained')

# Распаковываем словари в два массива
xs1, ys1 = zip(*aver_per_GF.items())
xs2, ys2 = zip(*aver_per_GO.items())
# Делаем по оси x значения подписей строковыми, для корректного отображения
xs1 = [str(i) for i in xs1]
xs2 = [str(i) for i in xs2]
# Вывод столбчатых диаграмм
axes[0].bar(xs1, ys1)
axes[1].bar(xs2, ys2)

axes[0].set_ylabel("Среднее количество решённых задач", fontsize=14, fontname='Georgia')
axes[0].set_xlabel("Номер факультетской группы", fontsize=14, fontname='Georgia')
axes[1].set_ylabel("Среднее количество решённых задач", fontsize=14, fontname='Georgia')
axes[1].set_xlabel("Номер группы по информатике", fontsize=14, fontname='Georgia')

pyplot.savefig("Task3.jpg")
pyplot.show()

import matplotlib.pyplot as pyplot

with open("students.csv") as file:
    data = [string for string in file.read().split('\n')]
    preps = {}
    groups = {}
    name_last = 0
    for i in range(len(data)):
        arr = data[i].split(';')
        name = int(arr[0][4])
        group = int(arr[1])
        mark = int(arr[2])
        if name != name_last:
            preps[name] = []
            preps[name].append(mark)
            name_last = name
        else: preps[name].append(mark)
        if groups.get(group):
            groups[group].append(mark)
        else:
            groups[group] = []
            groups[group].append(mark)

print(groups)
mosaic = '''
ABC
DEF
GGG
'''
fig = pyplot.figure(constrained_layout=True, figsize=(9, 9), dpi=200)
ax_dict = fig.subplot_mosaic(mosaic)
fig.suptitle("Оценки среди преподователей", fontsize=16, fontname='Georgia')
average_perprep_min = 10
name_min = ''
average_perprep_max = 0
name_max = ''
labels = [i for i in range(3, 11)]
string = '0ABCDEFG'

def func(pct):
    if int(pct) != 0:
        return f'{int(pct)}%'
    else: return None

for i in range(1, 8):
    sizes = [preps[i].count(j) for j in range(3, 11)]
    average = sum(preps[i]) / len(preps[i])
    if average_perprep_min > average:
        average_perprep_min = average
        name_min = f"Преподователь {i}"
    if average_perprep_max < average:
        average_perprep_max = average
        name_max = f"Преподователь {i}"
    ax_dict[string[i]].pie(sizes, startangle=90,
                           autopct=lambda pct: func(pct), radius=1)
    ax_dict[string[i]].set_title(f"Преподователь {i}", fontname='Serif')
    if i == 7:
        ax_dict[string[i]].legend(labels=labels, loc='right',
                                  bbox_to_anchor=(1.5, 0.5))

fig.savefig("Task31.jpg")

print("Халява: ", name_max)
print("Нехалява: ", name_min)

mosaic = '''
ABC
DEF
'''
fig2 = pyplot.figure(constrained_layout=True, figsize=(9, 6), dpi=200)
ax_dict2 = fig2.subplot_mosaic(mosaic)
fig2.suptitle("Оценки среди групп", fontsize=16, fontname='Georgia')
average_pergroup_min = 10
group_min = ''
labels = [i for i in range(3, 11)]
string = '0ABCDEF'

for i in range(1, 7):
    sizes = [groups[i + 750].count(j) for j in range(3, 11)]
    average = sum(groups[i + 750]) / len(groups[i + 750])
    if average_pergroup_min > average:
        average_pergroup_min = average
        group_min = f"Группа {i + 750}"
    ax_dict2[string[i]].pie(sizes, startangle=90,
                           autopct=lambda pct: func(pct), radius=1)
    ax_dict2[string[i]].set_title(f"Группа {i + 750}", fontname='Serif')
    if i == 6:
        ax_dict2[string[i]].legend(labels=labels, loc='right',
                                  bbox_to_anchor=(1.2, 0.5))
fig2.savefig("Task32.jpg")
print("Раздолбайская группа: ", group_min)
# pyplot.show()
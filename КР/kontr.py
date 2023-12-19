import numpy as np
import pandas as pd

N = int(input())
arr = [input().split(';')[1] for i in range(N)]
dictionary = {}
for i in range(N):
    arr[i] = arr[i].split(',')
    arr[i] = [item.lower().replace(' ', '') for item in arr[i]]
    for j in range(len(arr[i])):
        if f'{arr[i][j].split(":")[0]}' in dictionary:
            dictionary[f'{arr[i][j].split(":")[0]}'] += int(arr[i][j].split(":")[1])
        else:
            dictionary[f'{arr[i][j].split(":")[0]}'] = int(arr[i][j].split(":")[1])

dictionary = dict(sorted(dictionary.items()))
for key, value in dictionary.items():
    print(key, value)


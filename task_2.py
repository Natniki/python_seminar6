"""Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]"""

"""mylist = [-5, 9, 0, 3, -1, -2, 1,4, -2, 10, 2, 0, -9, 8, 10, -9,0, -5, -5, 7]
minEl = 2
maxEl = 9"""


def findEl(arr, miEl, maEl):
    newList = []
    for i in range(len(arr)):
        if arr[i] >= miEl and arr[i] <= maEl:
            newList.append(i)
    return  newList
        
myList = [-5, 9, 0, 3, -1, -2, 1,4, -2, 10, 2, 0, -9, 8, 10, -9,0, -5, -5, 7]
minEl = int(input("minimalnyj element: "))
maxEl = int(input("maximalnyj element: "))
result = findEl(myList, minEl, maxEl)
print(result, end=" ")
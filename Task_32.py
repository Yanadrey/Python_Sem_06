# Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

n = int(input("Введите количество элементов массива: "))
left_range = int(input("Введите нижнюю границу диапазона: "))
right_range = int(input("Введите верхнюю границу диапазона: "))

import random
array = [random.randint(-10,10) for i in range(n)]
array_index = []
for i in range(len(array)):
    if left_range <= array[i] <= right_range:
        array_index.append(i)

print(array)
print(array_index)        


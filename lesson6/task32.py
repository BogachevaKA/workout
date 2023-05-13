# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randrange
N = 20
A = [randrange(1, 20) for i in range(N)]
print(*A)

min_number = int(input('Введите минимальный диапазон: '))
max_number = int(input('Введите максимальный диапазон: '))

for i in range(len(A)):
    if min_number <= A[i] <= max_number:
        print(i, end =' ')
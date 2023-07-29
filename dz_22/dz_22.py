# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# Пример
# m = 11
# n = 6

# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18

# print(6 12)

m: int = int(input('Введите число 1 : '))
n: int = int(input('Введите число 2 : '))

from random import randint
m_mn1: int = [randint(1,20) for _ in range(m)]
n_mn2: int = [randint(1,20) for _ in range(n)]

print(f'{m_mn1}\n{n_mn2}')
m_mn1.sort()
n_mn2.sort()

unique_numbers = list(set(m_mn1))
unique_numbers2 = list(set(n_mn2))

newSpisok = []
for i in unique_numbers:
    if i in unique_numbers2:
        newSpisok.append(i)

print(f"Числа которые встречаются в обоих наборах : {newSpisok}")

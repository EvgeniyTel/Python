# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X .
# Если таких значений больше одного, вывести первый найденный.
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input("Введите количество элементов в массиве: "))
a = [i + 1 for i in range(n)]
print(a)
x = int(input("Введите искомое число: "))
result = []

for i in set(a):
    if x > 1:
        result = x - 1
    
print(f"Первый найденный: {result}")
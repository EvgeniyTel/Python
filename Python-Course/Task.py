# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
numb = int(input())
sum = 0
while numb > 0:
  ost = numb % 10
  sum += ost
  numb = numb // 10
print(sum)
  

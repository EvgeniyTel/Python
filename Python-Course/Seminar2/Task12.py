# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# Пример:
# Ввод: 5 6 -> 2 3
s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение чисел: '))
start = 1
end = 1000
step = 1
for x in range(start, end, step):
  for y in range(start, end, step):
    if s == x + y and p == x * y:
     print(f'Загаданные числа : {x} и {y}')
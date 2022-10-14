# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

from random import randint

counts = {}
result = []

strRnd = ''.join(list(list(map(str, [randint(0,9) for i in range(30)]))))
print(f'Заданная последовательность: {strRnd}')

for i in strRnd:
    if counts.get(i):
        counts[i] = counts.get(i) + 1
    else:
        counts[i] = 1

for i in counts.items():
    if i[1] == 1:
        result.append(int(i[0]))

print(f'Уникальные цифры последоватльности: {result}')

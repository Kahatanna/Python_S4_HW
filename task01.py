# Вычислить число ПИ c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

import math

def EnterFloat():
    number = 0
    while True:
        try:
            number = float(input('Введите значение точности d от 0.1 до 0.0000000001: '))
            if number not in d:
                print("Введеное значение не корректно, попробуйте еще раз")
                continue
            break
        except:
            print("Введеное значение не корректно, попробуйте еще раз")
    return number

d = []
for i in range(1, 11):
    d.append(1/(10**i))

dNum = EnterFloat()

print(round(math.pi, d.index(dNum)+1))
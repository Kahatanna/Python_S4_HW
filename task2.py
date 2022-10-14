# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def EnterInt():
    number = 0
    while True:
        try:
            number = int(input('Введите натуральное число N>=2: '))
            if number < 2:
                print("Введеное значение не корректно, попробуйте еще раз")
                continue
            break
        except:
            print("Введеное значение не корректно, попробуйте еще раз")
    return number

n = EnterInt()

result = []
minDel = 2
buf = n

while (minDel <= buf):
    if buf % minDel == 0:
        result.append(minDel)
        buf /= minDel
    else:
        minDel += 1
print(f'Список простых множителей числа {n}:')
print(set(result))
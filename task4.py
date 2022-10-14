# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

from random import randint

def createDict():
    eq = {}
    degree = int(input('Введите максимальную степень многочлена: '))
    for i in range(degree, -1, -1):
        eq[i] = randint(-10,10)
    return eq

def createEquation(eq: dict):
    strEq = ''
    first = True

    for k,v in eq.items():
        if first:
            first = False
            if v > 0:
                strEq += f'{v}*x^{k}'
            elif v < 0:
                strEq += f'-{abs(v)}*x^{k}'
        else:
            if v > 0:
                strEq += f' + {v}*x^{k}'
            elif v < 0:
                strEq += f' - {abs(v)}*x^{k}'
    return strEq

def printEquation(equation: str):
    print(equation.replace('*x^1', 'x').replace('*x^0', '') + ' = 0')

printEquation(createEquation(createDict()))
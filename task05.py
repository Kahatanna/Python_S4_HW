# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

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

def summEquation(equation1: dict, equation2: dict):
    finalEquation = {}

    for i in range(max(len(equation1), len(equation2)), -1, -1):
        if equation1.get(i) or equation2.get(i):
            finalEquation[i] = (equation1.get(i) if equation1.get(i) else 0) + (equation2.get(i) if equation2.get(i) else 0)
    return finalEquation

eq1 = createDict()
printEquation(createEquation(eq1))

eq2 = createDict()
printEquation(createEquation(eq2))

print(summEquation(eq1, eq2))
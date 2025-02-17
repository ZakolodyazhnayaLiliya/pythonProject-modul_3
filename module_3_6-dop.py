print('Дополнительное практическое задание по модулю: "Подробнее о функциях."')
# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
print ('Задание "Раз, два, три, четыре, пять .... Это не всё?":')
#
# Наши студенты, без исключения, - очень умные ребята. Настолько умные, что иногда по утру сами
# путаются в том, что намудрили вчера вечером.
#
# Один из таких учеников уснул на клавиатуре в процессе упорной учёбы (ещё и трудолюбивые).
# Тем не менее, даже после сна, его код остался рабочим и выглядел следующим образом:

# Увидев это студент задался вопросом: "А есть ли универсальное решение для подсчёта суммы всех чисел и длин всех строк?"
# Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре (списку, словарю и т.д.) по-разному.
# Помогите сокурснику осуществить его задумку.
# Что должно быть подсчитано:
# Все числа (не важно, являются они ключами или значениям или ещё чем-то).
# Все строки (не важно, являются они ключами или значениям или ещё чем-то)
# Для примера, указанного выше, расчёт вёлся следующим образом:
# 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99
# Входные данные (применение функции):
data_structure = [

[1, 2, 3],

{'a': 4, 'b': 5},

(6, {'cube': 7, 'drum': 8}),

"Hello",

((), [{(2, 'Urban', ('Urban2', 35))}])

]
# result = calculate_structure_sum(data_structure)
# print(result)
# Выходные данные (консоль):
# 99
# Примечания (рекомендации):
#
# Весь подсчёт должен выполняться одним вызовом функции.
# Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.
# Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
# Для определения типа данного используйте функцию isinstance.
from collections.abc import Iterable
def calculate_structure_sum(*args): # для функции задаем произвольное число параметров
    sum = 0
    for arg in args:
        if isinstance(arg, int) or isinstance(arg, float): # если число целое или дробное, то получаем сумму
            sum += arg
        elif isinstance(arg, str): #  если строка, то вычесляем длинну строки и складываем к сумме
            sum += len(arg)
        elif isinstance(arg, dict):
            keys, values = zip(*arg.items())
            arg=keys+values
            sum += calculate_structure_sum(*arg)
        elif isinstance(arg, Iterable): # если итерируемый объект то разбираем
            sum += calculate_structure_sum(*arg)

    return sum

result = calculate_structure_sum(data_structure)

print(result)
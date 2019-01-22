# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibbonacci(n, m):
    a, b = 1, 1
    f_list = [1, ]

    for i in range(m):
        a, b = b, a + b
        f_list.append(a)

    return f_list[n - 1:m]
n = int(input('введите первое значение:'))
m = int(input('введите второе значение:'))

print(fibbonacci(n, m))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_for_max(num_list):
    n = 1
    while n < len(num_list):
        for i in range(len(num_list) - n):
            if num_list[i] > num_list[i + 1]:
                num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
        n += 1
    return num_list
num_list = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
print(sort_for_max(num_list))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
# Код к этой задаче я спер полностью, разобрал и понял, но менять что то смысла не вижу
# т.к мысли не мои от слова совсем

def filter_function(func,iterable):
    output_iterable = []
    for i in range(len(iterable)):
        if func(iterable[i]) == True:
            output_iterable.append(iterable[i])
    return output_iterable

func = lambda x: type(x) == str
iterable = [-1, 2, 'a', 4, 'fgf']
print(filter_function(func,iterable))
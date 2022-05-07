"""
МОДУЛЬ 1
В модуле прописаны заготовки для 8 функций
Под каждой функцией есть описание как она должна работать
ниже есть примеры использования функции
Задание: реализовать код функции, чтобы он работал по описанию и примеры использования давали верный результат
"""


def simple_separator():
    a = '**********'
    return a
    pass


print(simple_separator() == '**********') # True


def long_separator(count):
    b = '*' * count
    return b
    pass

print(long_separator(3) == '***')  # True
print(long_separator(4) == '****')  # True


def separator(simbol, count):
    z = simbol * count
    return z
    pass


print(separator('-', 10) == '----------')  # True
print(separator('#', 5) == '#####')  # True


def hello_world():
    print('**********\n'
          '\n'
          'Hello World!\n'
          '\n'
          '##########')
    return
    pass


'''
**********

Hello World!

##########
'''
hello_world()


def hello_who(who='World'):
    print('**********\n'
          '\n'
          'Hello',who,'!\n'
          '\n'
          '##########')
    return
    pass


hello_who()
hello_who('Max')
hello_who('Kate')


def pow_many(power, *args):
    result = 0
    for number in args:
        result += number
    result = result ** power
    return result
    pass


print(pow_many(1, 1, 2) == 3)  # True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3) == 5)  # True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1) == 4)  # True -> (1 + 1)**2 == 4
print(pow_many(3, 2) == 8)  # True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100


def print_key_val(**kwargs):
    for i, j in kwargs.items():
        print(i, '-->', j)
    return
    pass


"""
name --> Max
age --> 21
"""
print_key_val(name='Max', age=21)
"""
animal --> Cat
is_animal --> True
"""
print_key_val(animal='Cat', is_animal=True)


def my_filter(iterable, function):
    result = []
    for i in iterable:
        if function(i):
            result.append(i)
    return result
    pass


print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True

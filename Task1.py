# Use
# def outer_function(x):
# def inner_function(y):  #

# return x + y  # Use outer f in inner.

# return inner_function  # return inner function


# # return sum(numbers):

# add_five = outer_function(5)  #  Створюемо замкнення с x = 5
# print(add_five(10))  # 15
# print(add_five(2))  # 7


def caching_fibonacci():
    cache = {}  # Створюємо кеш для зберігання обчислених значень

    def fibonacci(n):
        if n in cache:  # Перевіряємо, чи є значення в кеші
            return cache[n]  # функция повинна повертати значення кэша
        if n == 0:
            result = 0
        elif n == 1:
            result = 1
        else:
            result = fibonacci(n - 1) + fibonacci(
                n - 2
            )  # Рекурсивний виклик Использование рекурсии для вычисления чисел Фибоначчи.
        cache[n] = result  # Зберігаємо обчислене значення в кеш
        return result  # функция должна возвращать значение кэша

    return fibonacci  # Повертаємо внутрішню функцію


# Используем функцию fibonacci для вычисления чисел Фибоначчи
fibonacci = caching_fibonacci()
print(fibonacci(10))  # 55
print(fibonacci(15))  # 610

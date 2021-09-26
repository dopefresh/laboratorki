from functools import reduce
import time


def message_decorator(function):
    def wrapper(array):
        answer = function(array)
        if answer == 0:
            print("NO")
        elif answer >= 10:
            print("Too many")
    return wrapper


@message_decorator
def count_even(array):
    answer = [1 if number % 2 == 0 else 0 for number in array]
    return sum(answer)


def swap(function):
    def wrapper(x, y, show=False):
        return function(y, x, show)

    return wrapper


@swap
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res


def logging_decorator_maker(file_path):

    def logging_decorator(function):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = function(*args, **kwargs)
            working_time = time.time() - start_time
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f'function working time is {working_time}\n')
                f.write(f'function arguments are {args} and {kwargs}\n')
                f.write(f'function result is {result}')
            return result

        return wrapper
    return logging_decorator


@logging_decorator_maker('/home/vasilii/Desktop/python_learn/decorators/info.log')
def some_function(*args, **kwargs):
    return reduce((lambda x, y: x * y), *args)


print(some_function([100] * 10))

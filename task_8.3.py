from functools import wraps


def type_logger(func):

    @wraps(func)
    def wrapper(*x, **y):
        result = func(*x, **y)
        for i in x:
            print(f'{func.__name__}({i}: {type(i)})')

    return wrapper


@type_logger
def calc_cube(*x):
    new_x = list(x)
    for i in new_x:
        if isinstance(i, int) or isinstance(i, float):
            print(i ** 3)


a = calc_cube(5, 6, 8.9, "p")

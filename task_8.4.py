from functools import wraps


def val_checker(f_func):
    def _checker(func):

        @wraps(func)
        def wrapper(x):
            if f_func(x):
                msg = f'{func(x)})'
            else:
                raise ValueError(f'ValueError: wrong val {x}')

        return wrapper

    return _checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    print(x ** 3)
    # return x** 3


# x = 'op'
# x = 5
x = -5
try:
    a = calc_cube(x)
except ValueError as e:
    print(e)
except Exception:
    print(f'The argument is not a number.')

# https://samit.bearblog.dev/how-is-python-written/
# function overloading in python (not supported by default)

from inspect import getfullargspec
from functools import wraps


class OverloadRegistry:
    """Singleton class to hold overloaded functions"""

    _instance = None  # private

    def __init__(self) -> None:
        if OverloadRegistry._instance is not None:
            raise Exception("Use get_instance() to get singleton instance")
        self.registry = {}
        OverloadRegistry._instance = self

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = OverloadRegistry()
        return cls._instance

    def _make_key(self, fn, args=None):
        if args is None:
            args = getfullargspec(fn).args
        return (
            fn.__module__,
            fn.__name__,
            len(args),
        )  # key = {module, name, number of arguments} this helps us differentiate functions in overloading based on parameters

    # making a registry with this key
    def register(self, fn):
        key = self._make_key(fn)
        self.registry[key] = fn  # attach this key to function

        @wraps(fn)
        def wrapper(*args, **kwargs):
            """The @wraps decorator from Pythons functools module is used to preserve metadata of the original function when its being wrapped by another function (like in decorators)"""
            match_key = (fn.__module__, fn.__name__, len(args))
            target_fn = self.registry.get(match_key)
            if not target_fn:
                raise TypeError("No matching function of this type")
            return target_fn(*args, **kwargs)

        return wrapper


def overload(fn):
    return OverloadRegistry.get_instance().register(fn)


@overload
def area(l, b):
    return l * b


@overload
def area(r):
    return r**2 * 3.14


print(area(5, 6))  # 30
print(area(3))  # 28.8
"""
You're wrapping the original fn (the overloaded function) with wrapper. Without @wraps(fn), the wrapper would replace fn and you’d lose important information like:

    __name__ (function name)

    __doc__ (docstring)

    __module__ (module it's defined in)

    __annotations__

    and more
"""

# Function overloading using functools.singledispatch
from functools import singledispatch


@singledispatch
def area(shape):
    raise TypeError("Unsupported type")


@area.register
def _(dimensions: tuple):
    l, b = dimensions
    return l * b


@area.register
def _(radius: int):
    return 3.14 * radius**2


print(area((5, 6)))  # 30
print(area(3))  # 28.8


# Using singledispatchmethod (for methods) : OOP
from functools import singledispatchmethod


class AreaCalc:
    @singledispatchmethod
    def area(self, shape):
        # default case incase no matching type is registered
        # calc.area("triangle")  # ❌ Triggers this -> TypeError("Unsupported type")
        raise TypeError("Unsupported Type")

    # registry
    @area.register
    def _(self, dimensions: tuple):
        l, b = dimensions
        return l * b

    @area.register
    def _(self, radius: int):
        return 3.14 * radius**2


calc = AreaCalc()
print(calc.area((5, 6)))  # 30)
print(calc.area(3))  # 28.8)

def add(a, b):
    """Додає два числа"""
    return a + b


def subtract(a, b):
    """Віднімає від першого числа друге"""
    return a - b


def multiply(a, b):
    """Множення двох чисел."""
    return a * b


def divide(a, b):
    """Ділення першого числа на друге"""
    if b == 0:
        raise ZeroDivisionError

    return a / b

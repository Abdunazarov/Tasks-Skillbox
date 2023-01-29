
operators = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '**': lambda a, b: a ** b,
    '/': lambda a, b: a / b,
    '//': lambda a, b: a // b,
    '%': lambda a, b: a % b
}


class SimpleCalculator:
    # конструктор по умолчанию
    def __init__(self, *args: list):
        self.args = args
        # modified_args облегчит нам работу с написанием модулей как divide, divide_whole, power и modulo  
        self.modified_args = args[1:]
        
    # модуль который даст нам сумму чисел
    def add(self) -> int or float:
        result = 0
        for x in self.args:
            result += x
        return result

    # модуль для вычитания чисел
    def substract(self) -> int or float:
        return self.args[0]*2 - self.add()


    # модуль для умножения чисел 
    def multiply(self) -> int or float:
        result = 1
        for x in self.args:
            result *= x
        return result


    # модуль для деления чисел
    def divide(self) -> int or float:
        result = self.args[0]

        for x in self.modified_args:
            result /= float(x)
        return result


    # модуль для целочисленного деленя чисел
    def divide_whole(self) -> int:
        result = self.args[0]

        for x in self.modified_args:
            result //= x
        return result


    # модуль для возведения в степень
    def power(self) -> int or float:
        result = self.args[0]

        for x in self.modified_args:
            result **= x
        return result


    # модуль для вычисления остатка от деления
    def modulo(self) -> int:
        result = self.args[0]

        for x in self.modified_args:
            result %= x
        return result


calc = SimpleCalculator(100, 2, 2)
print(calc.divide())






# Наш класс SimpleCalculator может быть наследован новыи классом для дальнейшего расширения 
class AdvancedCalculator(SimpleCalculator):
    ...
    pass




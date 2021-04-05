from abc import ABC, abstractmethod
from math import sqrt as sq
import logging


class Operations(ABC):
    def __init__(self, num):
        try:
            self.num = float(num)
        except ValueError:
            cacl_logger.critical(f'Value "{num}" not number')
            self.num = None

    @abstractmethod
    def __add__(self, other):
        raise NotImplementedError('Method not implement!')

    @abstractmethod
    def __sub__(self, other):
        raise NotImplementedError('Method not implement!')

    @abstractmethod
    def __mul__(self, other):
        raise NotImplementedError('Method not implement!')

    @abstractmethod
    def __truediv__(self, other):
        raise NotImplementedError('Method not implement!')

    @abstractmethod
    def __pow__(self, num):
        raise NotImplementedError('Method not implement!')

    @abstractmethod
    def sqrt(self):
        raise NotImplementedError('Method not implement!')

    @abstractmethod
    def percent(self, per):
        raise NotImplementedError('Method not implement!')


class Calc(Operations):
    def __init__(self, num):
        super().__init__(num)

    def __add__(self, other):
        calc_logger.info(f'Called __add__ func with attr {self.num}, {other.num}')
        return self.num + other.num

    def __sub__(self, other):
        calc_logger.info(f'Called __sub__ func with attr {self.num}, {other.num}')
        return self.num - other.num

    def __mul__(self, other):
        calc_logger.info(f'Called __mul__ func with attr {self.num}, {other.num}')
        return self.num * other.num

    def __truediv__(self, other):
        calc_logger.info(f'Called __truediv__ func with attr {self.num}, {other.num}')
        try:
            result = self.num / other.num
        except ZeroDivisionError:
            calc_logger.critical(f'expression raise ZeroDivisionError')
            result = 'ZeroDivisionError'
        return result

    def __pow__(self, power):
        calc_logger.info(f'Called __pow__ func with attr {self.num}, {power.num}')
        try:
            result = self.num ** power.num
        except ZeroDivisionError:
            calc_logger.critical(f'expression raise ZeroDivisionError')
            result = 'ZeroDivisionError'
        return result

    def sqrt(self):
        calc_logger.info(f'Called sqrt func with attr {self.num}')
        try:
            result = sq(self.num)
        except ValueError:
            calc_logger.critical(f'Value {self.num} forbidden for this operation')
            result = f'Value {self.num} forbidden for this operation'
        return result

    def percent(self, other):
        calc_logger.info(f'Called percent func with attr {self.num}, {other.num}')
        if other.num < 0:
            calc_logger.warning(f'Percent value {other.num} should be positive')
            return 'Percent value should be positive'
        return self.num * other.num / 100

def create_logger(name):
    logger = logging.getLogger(name)

    f_handler = logging.FileHandler(name + '.log')

    f_handler.setLevel(logging.INFO)

    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    f_handler.setFormatter(f_format)

    logger.addHandler(f_handler)
    logger.setLevel(logging.INFO)
    return logger


def input_parser(input_str):
    calculator_error = f'expression "{input_str}" can`t be calculate'
    result = calculator_error
    calc_logger.info(f'Received expression is {input_str} ')
    expression = input_str.split(' ')

    if len(expression) == 1:
        if expression[0] == 'quit':
            calc_logger.info('Shutting down the calculator')
            return False
        result = calculator_error
    elif len(expression) == 2:
        if expression[0] == 'sqrt':
            a = Calc(expression[1])
            if a.num is not None:
                result = a.sqrt()
            else:
                result = calculator_error
    elif len(expression) == 3:
        if expression[1] in available_operations:
            a = Calc(expression[0])
            op = expression[1]
            b = Calc(expression[2])
            if (a.num is not None) and (b.num is not None):
                if op == '+':
                    result = a + b
                if op == '-':
                    result = a - b
                if op == '*':
                    result = a * b
                if op == '**':
                    result = a ** b
                if op == '/':
                    result = a / b
                if op == 'per':
                    result = a.percent(b)
    else:
        result = calculator_error
    if result == calculator_error:
        calc_logger.warning(f'Mistake in expression {input_str}')
    print(f'Result: {result}')
    return True
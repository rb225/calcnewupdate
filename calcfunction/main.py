""" This is the increment function"""
from calcfunction.calculations.addition import Addition
from calcfunction.calculations.multiplication import Multiplication
from calcfunction.calculations.subtraction import Subtraction
from calcfunction.calculations.division import Division
from calcfunction.history.historycalc import History


class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def add_numbers(*args):
        """ adds list of numbers"""
        calculation = Addition(args)
        History.add_calculation_to_history(calculation)
        return calculation.get_result()

    @staticmethod
    def subtract_numbers(*args):
        """ subtract a list of numbers from result"""
        calculation = Subtraction(args)
        History.add_calculation_to_history(calculation)
        return calculation.get_result()

    @staticmethod
    def multiply_numbers(*args):
        """ multiplication number from result"""
        calculation = Multiplication(args)
        History.add_calculation_to_history(calculation)
        return calculation.get_result()

    @staticmethod
    def divide_numbers(*args):
        """ Division number from result"""
        calculation = Division(args)
        History.add_calculation_to_history(calculation)
        return calculation.get_result()

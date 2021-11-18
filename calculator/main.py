"""Importing all methods from calc """
from calcfunction.addition import Addition
from calcfunction.subtraction import Subtraction
from calcfunction.multiplication import Multiplication
from calcfunction.division import Division


class Calculator:
    """ Creating calculator module"""
    history = []

    @staticmethod
    def clear_history():
        """ Clearing history"""
        Calculator.history.clear()

    @staticmethod
    def add_calculation_to_history(calculation):
        """ Appends calculation to history array """
        Calculator.history.append(calculation)

    @staticmethod
    def get_first_calculation_history():
        """ Gets first calculation from history array """
        return Calculator.history[0]

    @staticmethod
    def get_last_calculation_added():
        """ Gets last calculation from history array """
        return Calculator.history[-1]

    @staticmethod
    def get_calculation_count():
        """ Gets number of calculations from history array """
        return len(Calculator.history)

    @staticmethod
    def add_nums(value_a, value_b):
        """ Adding two numbers and storing it to history array """
        addition = Addition.create(value_a, value_b).getresult()
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_last_calculation_added()

    @staticmethod
    def subtract_nums(value_a, value_b):
        """Subtracting two numbers and storing it to history array"""
        subtraction = Subtraction.create(value_a, value_b).getresult()
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_last_calculation_added()

    @staticmethod
    def multiply_nums(value_a, value_b):
        """ Multiplying two numbers and storing it to history array"""
        multiplication = Multiplication.create(value_a, value_b).getresult()
        Calculator.add_calculation_to_history(multiplication)
        return Calculator.get_last_calculation_added()

    @staticmethod
    def divide_nums(value_a, value_b):
        """ dividing two numbers and storing it to history array """
        division = Division.create(value_a, value_b).getresult()
        Calculator.add_calculation_to_history(division)
        return Calculator.get_last_calculation_added()

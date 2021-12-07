""" Class for multiplication"""
from calcfunction.calculations.calculation import Calculation


class Multiplication(Calculation):
    """Multiplication calculation object"""

    def get_result(self):
        """Performing multiplication function for the values inheriting from the parent class"""
        result = 1.0
        for value in self.values:
            result = result * value
        return round(result, 3)

""" Class for division"""
from calcfunction.calculations.calculation import Calculation


class Division(Calculation):
    """Division calculation object"""

    def get_result(self):
        """Performing division function for the values inheriting from the parent class"""
        result = 1.0
        for value in self.values:
            result = value / result
        return result

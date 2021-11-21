"""Class for addition"""
from calcfunction.calculations.calculation import Calculation


class Addition(Calculation):
    """ calculation addition class"""

    def get_result(self):
        """Return  the addition results"""
        sum_of_values = 0.0
        for value in self.values:
            sum_of_values = value + sum_of_values
        return sum_of_values

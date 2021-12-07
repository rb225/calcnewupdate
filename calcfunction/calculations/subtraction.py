""" Class for subtraction"""
import pprint

from calcfunction.calculations.calculation import Calculation


class Subtraction(Calculation):
    """subtraction calculation object"""

    def get_result(self):
        """Return the subtraction results"""
        difference_of_values = self.values[0]
        for value in self.values[1:]:
            difference_of_values = difference_of_values - value
            pprint.pprint(value)
        return round(difference_of_values, 3)

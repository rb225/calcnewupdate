"""Importing parent class"""

from calcfunction.calculation import Calculation


# This is the multiplication function
class Multiplication(Calculation):
    """ Performing multiplication by taking two values from parent class"""
    def getresult(self):
        """ Returning the generated result """
        return self.value_a * self.value_b

"""Importing parent class"""

from calcfunction.calculation import Calculation


# This is the division function
class Division(Calculation):
    """ Performing division by taking two values from parent class"""
    def getresult(self):
        """ Returning the generated result """
        return self.value_a / self.value_b

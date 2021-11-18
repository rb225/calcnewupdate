"""Calculation Initial  class """


class Calculation:
    """ Defining constructor class"""

    # pylint: disable=too-few-public-methods
    def __init__(self, value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b

    # class factory method
    @classmethod
    def create(cls, value_a, value_b):
        """ Returning the values """
        return cls(value_a, value_b)

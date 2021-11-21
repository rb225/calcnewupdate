""" import all the methods from calc_methods"""


class History:
    """ Creating a Module Calculator """
    # result set to 0 for initialization
    history = []

    @staticmethod
    def clear_history():
        """ Clearing the array of the history"""
        History.history.clear()

    @staticmethod
    def add_calculation_to_history(calculation):
        """ Appending the calculated values in the history list """
        History.history.append(calculation)

    @staticmethod
    def get_first_calculation_history():
        """ Returning the first stored value in the history list """
        return History.history[0]

    @staticmethod
    def get_last_calculation_added():
        """ Returning the last stored value in the history list """
        return History.history[-1]

    @staticmethod
    def get_calculation_count():
        """ Returning the count of the values stored in the history list """
        return len(History.history)

""" This is the increment function"""
import logging
import sys
from calcfunction.calculations.addition import Addition
from calcfunction.calculations.multiplication import Multiplication
from calcfunction.calculations.subtraction import Subtraction
from calcfunction.calculations.division import Division
from calcfunction.history.historycalc import History
from calcfunction.csv_handle.read_csv import CSVRead


sys.tracebacklimit = 0
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('calcfunction/log/sample.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


class Calculator:
    """ This is the Calculator class"""
    # result set to 0 for initialization
    history = []
    data = []
    path = ''

    def __init__(self, path):
        self.data = CSVRead.read_data(path)
        self.path = path
        self.move_path = path.replace("input", "done")

    def get_data(self):
        """ Splits the data and returns all columns """
        csv_data = self.data
        num1 = csv_data['Num1'].values
        num2 = csv_data['Num2'].values
        add = [round(i, 3) for i in csv_data['Add'].values]
        sub = [round(i, 3) for i in csv_data['Subtract'].values]
        multi = [round(i, 3) for i in csv_data['Multiply'].values]
        div = [round(i, 3) for i in csv_data['Divide'].values]

        return num1, num2, add, sub, multi, div

    @staticmethod
    def add_numbers(*args):
        """ adds list of numbers"""
        addition = Addition(args).get_result()
        logger.debug('Add: %f + %f = %f', args[0], args[1], addition)
        History.add_calculation_to_history(addition)
        return History.get_last_calculation_added()

    @staticmethod
    def subtract_numbers(*args):
        """ subtract a list of numbers from result"""
        calculation = Subtraction(args).get_result()
        logger.debug('Subtract: %f - %f = %f', args[0], args[1], calculation)
        History.add_calculation_to_history(calculation)
        return History.get_last_calculation_added()

    @staticmethod
    def multiply_numbers(*args):
        """ multiplication number from result"""
        calculation = Multiplication(args).get_result()
        logger.debug('Multiply: %f * %f = %f', args[0], args[1], calculation)
        History.add_calculation_to_history(calculation)
        return History.get_last_calculation_added()

    @staticmethod
    def divide_numbers(*args):
        """ Division number from result"""
        calculation = Division(args).get_result()
        logger.debug('Divide: %f / %f = %f', args[0], args[1], calculation)
        History.add_calculation_to_history(calculation)
        return History.get_last_calculation_added()

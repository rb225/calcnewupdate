""" importing files"""
import pprint
import pytest
from calculator.main import Calculator


# this is for fixture

@pytest.fixture()
def clear_history():
    """Clearing the history"""
    Calculator.clear_history()


def test_calculator_add(clear_history):
    """To check the addition results"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_nums(10, 20) == 30
    assert Calculator.add_nums(20, 20) == 40
    assert Calculator.add_nums(20, 30) == 50
    assert Calculator.add_nums(30, 40) == 70
    assert Calculator.get_calculation_count() == 4
    assert Calculator.get_first_calculation_history() == 30
    pprint.pprint(Calculator.history)

def test_calculator_subtract(clear_history):
    """ To check if calculator subtraction result is correct """
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.subtract_nums(10, 20) == -10
    assert Calculator.get_calculation_count() == 1
    pprint.pprint(Calculator.history)


def test_calculator_multiply(clear_history):
    """ To check if calculator multiplication result is correct """
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.multiply_nums(10, 20) == 200
    assert Calculator.get_calculation_count() == 1
    pprint.pprint(Calculator.history)


def test_calculator_divide(clear_history):
    """ To check if calculator division result is correct """
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.divide_nums(20, 20) == 1
    assert Calculator.get_calculation_count() == 1
    pprint.pprint(Calculator.history)

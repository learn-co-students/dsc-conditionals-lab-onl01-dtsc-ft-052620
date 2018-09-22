# importing testing framwork
import pytests

# importing objects from the jupyter notebook here
from ipynb.fs.full.index import is_it_hot, day_of_the_week, ends_with, bigger_number

# format for writing tests
# all functions that are to be run by test suite *must* be prepended with test_
def test_is_it_hot():
    assert is_it_hot is not None, "Make sure to set up your conditional so that it re-assigns the value for `is_it_hot`"
    assert is_it_hot == "It is so hot out!", "Remember any temperature above 80 degrees should assign the value `It is so hot out!`"

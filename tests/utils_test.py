
# this is the "tests/utils_tests.py" file...

from app.utils import to_usd
# this invokes the function we want to test

# Example test format
#def test_answer():
#    assert func(3) == 5


def test_to_usd():
    # it rounds to two decimal places (and have a dollar sign):
    assert to_usd(0.45555) == "$0.46"

    # if larger number, should use thousands seperator:
    assert to_usd(123456789.98) == "$123,456,789.98"
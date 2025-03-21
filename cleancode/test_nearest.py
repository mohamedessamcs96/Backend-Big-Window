from tests import nearest_square
from tests import sumNumbers

def test_nearest_square_5():
    assert(nearest_square(5)==4)


def test_nearest_square_4():
    assert(nearest_square(16)==16)


def test_sum():
    assert(sumNumbers(5,3)==7)
import pytest
from cal import Culculyator
cal = Culculyator()
def plus_test():
    assert cal.plus(1, 2) == 3
def minus_test():
    assert cal.minus(1000, 7) == 993
def mnoj_test():
    assert cal.mnoj(2, 2) == 4
def delit_test():
    assert cal.delit(4, 2) == 2
    assert cal.delit(10, 0) == "Нельзя делить на 0"
def stepen_test():
    assert cal.stepen(2, 2) == 4
    assert cal.stepen(0, -7) == "Нельзя возводить 0 в отрицательную степень"


plus_test()
minus_test()
mnoj_test()
delit_test()
stepen_test()
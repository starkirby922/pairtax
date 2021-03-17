import math
import taxcalcv4
import pytest
from unittest import mock
import builtins
#pip install pytest
#to run type "pytest test_taxcalcv4.py" in terminal


def test():
    #replace the numbers with government tax website
    #300000 200000 is self and spouce income
    with mock.patch.object(builtins, 'input', lambda _: '3000000 2000000'):
        #743800 and 744600 is serprate and joint income
        assert taxcalcv4.func() == [743800, 744600]


def test1():
    with mock.patch.object(builtins, 'input', lambda _: '500000 300000'):
        assert taxcalcv4.func() == [50920, 67510]

def test2():
    with mock.patch.object(builtins, 'input', lambda _: '450000 620000'):
        assert taxcalcv4.func() == [94900, 112900]

def test3():
    with mock.patch.object(builtins, 'input', lambda _: '100000 0'):
        assert taxcalcv4.func() == [0, 0]

def test4():
    with mock.patch.object(builtins, 'input', lambda _: '200000 150000'):
        assert taxcalcv4.func() == [1690, 2110]

def test5():
    with mock.patch.object(builtins, 'input', lambda _: '3000000 2000000'):
        assert taxcalcv4.func() == [743800 , 744600]


def test6():
    with mock.patch.object(builtins, 'input', lambda _: '534500 120000'):
        assert taxcalcv4.func() == [47365 , 44305]

def test7():
    with mock.patch.object(builtins, 'input', lambda _: '123000 50000'):
        assert taxcalcv4.func() == [0 , 0]

def test8():
    with mock.patch.object(builtins, 'input', lambda _: '6000000 0'):
        assert taxcalcv4.func() == [897300 , 897300]

def test9():
    with mock.patch.object(builtins, 'input', lambda _: '6000000 3000000'):
        assert taxcalcv4.func() == [1344600 , 1344600]

def test10():
    with mock.patch.object(builtins, 'input', lambda _: '4000000 278000'):
        assert taxcalcv4.func() == [604510 , 636915]

def test11():
    with mock.patch.object(builtins, 'input', lambda _: '240000 656800'):
        assert taxcalcv4.func() == [71916 , 84476]

def test12():
    with mock.patch.object(builtins, 'input', lambda _: '768000 999000'):
        assert taxcalcv4.func() == [213390 , 231390]

def test13():
    with mock.patch.object(builtins, 'input', lambda _: '534534 534534'):
        assert taxcalcv4.func() == [94740 , 112741]

def test14():
    with mock.patch.object(builtins, 'input', lambda _: '599999 534534'):
        assert taxcalcv4.func() == [105869 , 123870]

def test15():
    with mock.patch.object(builtins, 'input', lambda _: '599999 534534'):
        assert taxcalcv4.func() == [105869 , 123870]

def test16():
    with mock.patch.object(builtins, 'input', lambda _: '522000 287000'):
        assert taxcalcv4.func() == [53305 , 69150]

def test17():
    with mock.patch.object(builtins, 'input', lambda _: '217800 217800'):
        assert taxcalcv4.func() == [4988 , 8982]

def test18():
    with mock.patch.object(builtins, 'input', lambda _: '217800 129000'):
        assert taxcalcv4.func() == [2494 , 1927]

def test19():
    with mock.patch.object(builtins, 'input', lambda _: '676780 129000'):
        assert taxcalcv4.func() == [71552 , 69946]



    
#!/usr/bin/env python3
"""
test calculator
"""
from calculator import add, subtract  # , multiply


class TestCalculator:

    def test_add(self):
        assert 10 == add(4, 6)

    def test_subtract(self):
        assert 2 == subtract(6, 4)

#    def test_multiply(self):
#        assert 24 == multiply(2, 3, 4)

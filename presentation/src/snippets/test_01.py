# test_01.py
from unittest import TestCase

class ThisIsATest(TestCase):
    def test_addition_is_commutative(self):
        self.assertEqual(2 + 4, 4 + 2)

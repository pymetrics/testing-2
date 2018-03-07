# test_02.py
from unittest import TestCase

class BadTest(TestCase):
    def test_subtraction_is_commutative(self):
        self.assertEqual(4 - 2, 2 - 4)

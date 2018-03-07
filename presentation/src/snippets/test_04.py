# test_04.py
from unittest import TestCase

class Five:
    def __add__(self, other):
        return 5 + other


class TestNoTypeErrorExceptions(TestCase):
    def test_vague(self):
        # This will work, but what actually are we testing?
        five = Five()
        five + 1

    def test_addition_is_unexceptional(self):
        # but this expresses intent
        five = Five()
        try:
            five + 1
        except TypeError:
            self.fail("Addition caused a TypeError :(")

# test_03.py
from unittest import TestCase

class ExceptionalTest(TestCase):
    def test_io_error(self):
        with self.assertRaises(IOError):
            open("this_does_not_exist.txt")

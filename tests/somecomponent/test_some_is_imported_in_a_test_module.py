import unittest

from somecomponent.some import Something, show

class TestSome(unittest.TestCase):

    def test_some(self):
        show(__package__)
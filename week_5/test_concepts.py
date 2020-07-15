#unit tests
import re

def rearrange_name(name):
    result = re.search(r'^([\w .]*), ([\w .]*)', name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

>>> from rearrange import rearrange_name
>>> rearrange_name("Lovelace, Ada")
'Ada Lovelace'

#writing unittests in python
from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = 'Lovelace, Ada'
        expected = 'Ada Lovelace'
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase = "Hoopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase), expected)


unittest.main()

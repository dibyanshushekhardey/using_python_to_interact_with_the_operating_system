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

#errors - raising value error
def validate_user(username, minlen):
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen:
        return  False
    if not username.isalnum():
        return False
    return True

>>>print(validate_user("", -1))
Traceback (most recent call last):
  File "C:/Users/Hp/PycharmProjects/modules/16 july/valudate.py", line 10, in <module>
    print(validate_user("", -1))
  File "C:/Users/Hp/PycharmProjects/modules/16 july/valudate.py", line 3, in validate_user
    raise ValueError("minlen must be at least 1")
ValueError: minlen must be at least 1
>>>print(validate_user("", 1))
False
>>>print(validate_user("myuser", 1))
True
>>>print(validate_user("88", 1))
True
>>>print(validate_user(["name"], 1))
Traceback (most recent call last):
  File "C:/Users/Hp/PycharmProjects/modules/16 july/valudate.py", line 11, in <module>
    print(validate_user(["name"], 1))
  File "C:/Users/Hp/PycharmProjects/modules/16 july/valudate.py", line 6, in validate_user
    if not username.isalnum():
AttributeError: 'list' object has no attribute 'isalnum'

#assert function user
def validate_user(username, minlen):
    assert type(username) == str, "username must be a string"
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen:
        return  False
    if not username.isalnum():
        return False
    return True
>>>print(validate_user([8], 1))
Traceback (most recent call last):
  File "C:/Users/Hp/PycharmProjects/modules/16 july/valudate.py", line 12, in <module>
    print(validate_user([8], 1))
  File "C:/Users/Hp/PycharmProjects/modules/16 july/valudate.py", line 2, in validate_user
    assert type(username) == str, "username must be a string"
AssertionError: username must be a string

#testing for expected errors
import unittest

from validations import validate_user

class TestValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_user("validuser", 3), True)

    def test_too_short(self):
        self.assertEqual(validate_user(("inv", 5), False))

    def test_invalid_characters(self):
        self.assertEqual(validate_user("invalid_user", 1), False)

    def test_invalid_minlen(self):
        self.assertRaises(ValueError, validate_user, "user", -1)


# run tests
unittest.main()

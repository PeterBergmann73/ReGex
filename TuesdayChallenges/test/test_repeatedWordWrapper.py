import unittest
from unittest import TestCase

from challenge1 import RepeatedWordWrapper

wrapper = RepeatedWordWrapper()


def wrap1(text):
    return wrapper.wrap1(text)


# input -> expected
test1 = ('This is a test', 'This is a test')
test2 = ('This is is a test', 'This is <strong>is</strong> a test')
test3 = ('This test test is is', 'This test <strong>test</strong> is <strong>is</strong>')
test4 = ('This test is a test', 'This test is a test')

tests = [test1, test2, test3, test4]


class TestRepeatedWordWrapper(TestCase):

    # please, note the method has only self as a parameter.
    def test_wrap1(self):
        for test in tests:
            print(test)
            res = wrap1(test[0])
            print(res)
            self.assertEqual(wrap1(test[0]), test[1])

if __name__ == '__main__':
    unittest.main()
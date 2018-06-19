import unittest
from unittest import TestCase

import challenges


class TestChallenges(TestCase):

    def test_contains_wrong_char(self):
        str1 = 'ABCDEFabcdef123450'
        res1 = challenges.is_char_allowed(str1)
        self.assertEqual(res1, True)

        str2 = '*&%@#!'
        res2 = challenges.is_char_allowed(str2)
        self.assertEqual(res2, False)


    def test_text_match(self):
        str1 = 'ac'
        res1 = challenges.text_match(str1)
        self.assertEqual(res1, 'a')

        str2 = 'abc'
        res2 = challenges.text_match(str2)
        self.assertEqual(res2, 'ab')

if __name__ == '__main__':
    unittest.main()

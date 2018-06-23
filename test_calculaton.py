import calculation
import unittest

class HangmanTestCase(unittest.TestCase):

    def test_user_input(self):
        result = calculation.user_input()
        self.assertEqual(result, "A")


import calculation
import unittest

class HangmanTestCase(unittest.TestCase):

    def test_user_input(self):
        result = calculation.user_input()
        self.assertEqual(result, "A")


    def test_process_word(self):
        processedWord, result = calculation.process_word("STOCKHOLM")
        self.assertEqual(processedWord, ['S', 'T', 'O', 'C', 'K', 'H', 'O', 'L', 'M'])
        self.assertEqual(result, ['*', '*', '*', '*', '*', '*', '*', '*', '*'])


    def test_guess_letter(self):
        word, result = calculation.guess_letter("H", ['P', 'Y', 'T', 'H', 'O', 'N'], ['*', '*', '*', '*', '*', '*'])
        self.assertEqual(result, ['*', '*', '*', 'H', '*', '*'])




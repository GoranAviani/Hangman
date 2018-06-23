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


    def test_check_if_solved(self):
        word, result = calculation.check_if_solved(['P', 'Y', 'T', 'H', 'O', 'N'], ['*', '*', '*', 'H', '*', '*'])
        self.assertEqual(word, ['P', 'Y', 'T', 'H', 'O', 'N'])
        self.assertEqual(result, ['*', '*', '*', 'H', '*', '*'])

    def test_check_if_solved_it_is_solved(self):
        word, result = calculation.check_if_solved(['P', 'Y', 'T', 'H', 'O', 'N'], ['P', 'Y', 'T', 'H', 'O', 'N'])
        self.assertEqual(word, ['P', 'Y', 'T', 'H', 'O', 'N'])
        self.assertEqual(result, 'solved')


"""
# Check if the word is solved, if there are still '*' in the result var that means it is not solved.
def check_if_solved(word, result):
    if '*' in result:
        return (word, result)
    else:
        result = 'solved'
        return (word, result)
"""



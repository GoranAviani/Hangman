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


"""
#Processes the word to a list for further use, and make result list
def process_word(word):
    processedWord =[]
    result = []

    for x in word:
        processedWord.append(x)
        result.append('*')

    return (processedWord, result)
"""
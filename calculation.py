import random

def user_input():
    userInput = input('Enter one letter: ')
    userInput = userInput.upper()
    return userInput

#Processes the word to a list for further use, and make result list
def process_word(word):
    processedWord =[]
    result = []

    for x in word:
        processedWord.append(x)
        result.append('*')

    return (processedWord, result)

#Randomly choose one word from the list of words
def choose_word(wordList):
    return(random.choice(wordList))


#If the given letter is in the word , result is returned in format ex. ***A*
def guess_letter(userInput, word, result):

    for pos, x in enumerate(word):
        if x == userInput:
            result[pos] = x

    return(word, result)

#Check if the word is solved, if there are still '*' in the result var that means it is not solved.
def check_if_solved(word, result):
    if '*' in result:
        return(word, result)
    else:
        result = 'solved'
        return(word, result)


def add_new_word(wordList):
    print("*** Hangman Editor ***\n--------------------------------------------------\nEnter new word or type [B] to go [B]ack.")
    userNewWord = input("Command: ")

    if userNewWord.upper() == "B":
        return wordList
    else:
        while True:
            userConfirmation = input("Are you sure you want to add {} to Hangman? Type [Y]es or [N]o: ".format(userNewWord))
            if userConfirmation.upper() == "Y":
                wordList.append(userNewWord.upper())
                print("Word {} succesfully added".format(userNewWord))
                return wordList
            elif userConfirmation.upper() == "N":
                print("OK the word wont be added")
                return wordList
            else:
                print("I dont undestand the command.")


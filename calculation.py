import random
import json

#User input is processed
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

#Adding new word to the word list
def add_new_word(wordList):
    #print("rici" + ''.join(wordList))
    print("*** Hangman Editor ***\n--------------------------------------------------\nEnter new word or type [B] to go [B]ack.")
    userNewWord = input("Command: ")


    #If user wants back just return to main menu with the wordlist
    if userNewWord.upper() == "B":
        return wordList
    else:
        while True:
            #Checking if word alredy exists in memory
            checkMessage, wordList = check_if_word_exists(userNewWord, wordList)
            if checkMessage == "OK":

                #confirmation of adding word
                userConfirmation = input("Are you sure you want to add {} to Hangman? Type [Y]es or [N]o: ".format(userNewWord))
                #if confirmed add the word and return to main menu
                if userConfirmation.upper() == "Y":
                    #print("rici" + ''.join(wordList))
                    wordList.append(userNewWord.upper())
                    print("Word {} succesfully added".format(userNewWord))
                    return wordList
                #if not confirmed return to main manu
                elif userConfirmation.upper() == "N":
                    print("OK the word won't be added")
                    return wordList
                else:
                    print("I don't undestand the command.")

            else:
                print(checkMessage)
                return wordList

# Checking if word is already in the game memory.
def check_if_word_exists(userNewWord, wordList):
    print("user new word je {}".format(userNewWord))
    if str(userNewWord.upper()) in wordList:
        return("There is already '{}' in the memory!".format(userNewWord)), wordList
    else:
        return ("OK"), wordList


def save_to_file(wordList):
    with open('hangman.memory', 'w') as file:
        json.dump(wordList, file)
        file.close()

def load_from_file():
    with open('hangman.memory', 'r') as file:
        wordList = json.load(file)

    file.close()
    return wordList
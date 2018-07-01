import calculation

def list_words(wordList):
    print("\n\n       ***List of words in the game:***\n\n-------------------------------------------------------\n\n" + ', '.join(wordList) + "\n-------------------------------------------------------")
    anyKey = input("\n\n***Press any key and press Enter to return to main menu***")

    if len(anyKey) > 0:
        return wordList


def main_menu():
    userCommand = input("\n\n       ***Wellcome to Hangman's MAIN MENU!***\n\n-------------------------------------------------------\n* If you want to add new words to Hangman enter [N]\n* IF you want to list all word enter [L]"
                        "\n* If you want to start the game enter [G]\n* Enter [X] to exit game*\n-------------------------------------------------------"
                        "\n\nYour command: ")
    return userCommand



def main():
    wordList = (calculation.load_from_file())

    word = calculation.choose_word(wordList)
    word, result = calculation.process_word(word)

    isGameFinished = False
   # userCommand = main_menu()

    while True:
        #If the player guessed the challenge exit
        if isGameFinished == True:
            break
        userCommand = main_menu()

        #add new words
        if userCommand.upper() == "N":
            wordList = calculation.add_new_word(wordList)
            calculation.save_to_file(wordList)

        elif userCommand.upper() == "L":
            wordList = list_words(wordList)

        elif userCommand.upper() == "X":
            print("Good bye!")
            break


        #start game
        elif userCommand.upper() == "G":
            roundCounter = 0
            while True:
                print("\n\n-------------------------------------------------------\nGame status: {}\n".format(' '.join(result)))
                userInput = calculation.user_input()

                if userInput.upper() == "EXIT":
                    print("Good bye!")
                    break

                #Checking if userInput is a letter
                if userInput.isalpha():
                    userInput = userInput.upper()
                    #check if there is just on letter in userInfo
                    if len(userInput) > 1:
                        print('Only one letter please!')

                    elif userInput in word:
                        roundCounter += 1
                        word, result = (calculation.guess_letter(userInput, word, result))
                        #Checking if the word is solved
                        word, result = calculation.check_if_solved(word, result)

                        if result == 'solved':
                            print("Bravo!, the word was {0} and you solved it in {1} tries!" .format((''.join(word)), roundCounter))
                            #To exit other while loop
                            isGameFinished = True
                            break
                        else:
                            print("Number of tries {}.".format(roundCounter))
                        #print(word)
                        #print("Current status: {}".format(' '.join(result)))

                    elif userInput not in word:
                        roundCounter += 1
                        print("Good try but {} is not in the word!". format(userInput))
                        print("Number of tries {}.".format(roundCounter))
                else:
                    print('Letter only please!')
            else:
                print("I don't understand that command.")


if __name__ == '__main__':
    main()
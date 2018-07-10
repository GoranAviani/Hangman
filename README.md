# Hangman

![TextSeek](https://i0.wp.com/www.thegamegal.com/wp-content/uploads/2011/06/hangman-game-4.png?ssl=1)


## Description

Hangman is a paper and pencil guessing game for two players. One player thinks of a word and the other tries to guess it by suggesting letters or numbers, within a certain number of guesses.

This version of Hangman is single-player so the game picks randomly a word from the memory.

Words in the memory can be added by player from the Main menu.

## Main Menu

From the main menu player can start the game, enter new words in game memory, list all the words in the game memory or exit the game.


Preview:


`***Wellcome to Hangman's MAIN MENU!***`

`-------------------------------------------------------`


`* If you want to add new words to Hangman enter [N]`

`* IF you want to list all word enter [L]`

`* If you want to start the game enter [G]`

`* Enter [X] to exit game*`

`-------------------------------------------------------`



## Input description

To find wanted word you must to type in one letter at a time.

## Output description

<br>
If the input letter is in the word you will see the wanted word with that letter/s on their positions.

<br>

Example:

`Game status: S * * * K * * * *`

<br>
<br>

If the letter is not in the word you will see proper response with the number of tries you have taken.

<br>

Example:

`Good try but X is not in the word!`

`Number of tries 2.`


## Notes/ Additional Info

* Once the player inputed wrongly number of letters that are two times the length of word (2 * len(word)) the game is over because player has used all his turns.
# Are you ready to create the “Hangman” game  in Python?
# Let's give it a try. 

''' Task 1:  Import the module '''

# To create the Hangman game, you will import the hangmanfunc module.
# The hangmanfunc module has pre-built functions which are:
# - getclues() - Creates the placeholders for the word and returns the same
# - getword() - Randomly picks the word that needs to be guessed
# - check_clues_left() - Return True if there are characters of the word that still need to be guessed
# - update_clue()- Updates the character guessed right by the player
# - getstickmen()-Builds the hangman as the guesses go wrong
# Note: These functions have been made using lists. This is covered in Python Module 2.
# Uncomment the statements below:

import hangmanfunc
clues=hangmanfunc.getclues()
secret_word=hangmanfunc.getword()

# Observe the code.
# clues is the variable that has the placeholder for the variable.
# secret_word is the randomly picked up word that needs to be guessed.

''' Task 2: Create the hangman function '''
# Uncomment the statements below.
# Some of the comments have code instructions that you need to complete
# Click Run after completing all the instructions


def hangman():
# Instruction 1: Set the cnt to 6
  cnt= 6
  while cnt>=0:
# Instruction 2: Print the clues   
    print(clues)
    y=hangmanfunc.check_clues_left(clues)
    if y==True:
# Instruction 3: Get the character to guess as an input from user
     guess=input("Enter the letter you guess: ")
     if guess in secret_word:
        hangmanfunc.update_clue(guess,secret_word,clues)
     else:
# Instruction 4: Decrement cnt by 1
        cnt=cnt-1
        print(hangmanfunc.getstickmen(cnt)) 
    else:
      print("Awesome. You got the word. The secret word was -----",secret_word)
      break   
  else:
   print("Better luck next time. The secret word was -----",secret_word)
# Instruction 5: Call the hangaman function
hangman()   


''' Awesome!! That's a lovely game you have developed!! '''


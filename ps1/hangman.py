from ast import IsNot
import random
import string


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open("words.txt", 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
  '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    ''' 
  for i in secret_word:
    if i not in letters_guessed:
      return False 
  return True


def get_guessed_word(secret_word, letters_guessed):
  '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
  '''
  current_guess=""
  for i in secret_word:
    if i in letters_guessed:
      current_guess+=i
    else:
      current_guess+=" _ "
  return current_guess


def get_available_letters(letters_guessed):
  '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
  '''
  import string
  alphabets=string.ascii_lowercase
  unguessed=""
  for i in alphabets:
    if i not in letters_guessed:
      unguessed+=i
    else:
      unguessed+=""
  return unguessed


    

def hangman(secret_word):
  print('Welcome to the game, Hangman!')
  print('I am thinking of a word that is', len(secret_word), "letters long.")
  no_of_guesses=6
  letters_guessed=[]
  while no_of_guesses>0:
    if is_word_guessed(secret_word,letters_guessed)==True:
      print('------------')
      print('Ayeeee, You Won boiiii')
      break
    else:
      print('------------')
      print("You have ",no_of_guesses," guesses left")
      print("Available letters are",get_available_letters(letters_guessed))


      user_guess=input("Guess a letter homie: ")
      warning=2
      print("You have", warning+1, "warnings left")
      while warning>0:
        if user_guess.isalpha()==False or len(user_guess)>1:
          warning-=1
          print("That ain't a letter, you got ",warning+1," warnings left")
          user_guess=input("Guess a letter homie: ")
        else:
          break
      if warning==0:
        no_of_guesses-=1
        print("you have", no_of_guesses, "guesses left")
      user_guess.lower()


      if user_guess in secret_word and user_guess not in letters_guessed:
        letters_guessed.append(user_guess)
        print("Ayeeeeee great guess homie: ", get_guessed_word(secret_word,letters_guessed))
      elif user_guess in letters_guessed:
        print("Damnnnn homie, you've guessed this one already: ", get_guessed_word(secret_word,letters_guessed))
      elif user_guess not in secret_word:
        print("Damnnnn homie, this letter ain't in ma word: ", get_guessed_word(secret_word,letters_guessed))
        letters_guessed.append(user_guess)
        no_of_guesses-=1
    if no_of_guesses==0:
      print('------------')
      print("Game Over")
      print("No guesses left")
      print("Loser oof")
      print("The correct word was ", secret_word)
      break
    else:
      continue


def match_with_gaps(my_word, other_word):
  '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
  '''
  my_word.replace(' ','')
  if len(my_word)!=len(other_word):
      return False
  list_word=[]
  for i in range(0, len(my_word)):
    if my_word[i]=='_':
      list_word.append('_')
    else:
      list_word.append(other_word[i])
 
    if my_word==''.join(list_word):
        return True
  return False


def show_possible_matches(my_word):
  '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

  '''
  word_match=[]
  for guess_word in wordlist:
    if match_with_gaps(my_word,guess_word) is True:
      word_match.append(guess_word)
  if len(word_match)==0:
    return 'Word aint there'
  return word_match


def hangman_with_hints(secret_word):
  '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
  '''
  print('Welcome to the game, Hangman!')
  print('I am thinking of a word that is', len(secret_word), "letters long.")
  no_of_guesses=6
  letters_guessed=[]
  word_guess=''
  while no_of_guesses>0:
    if is_word_guessed(secret_word,letters_guessed)==True:
      print('------------')
      print('Ayeeee, You Won boiiii')
      break
    else:
      print('------------')
      print("You have ",no_of_guesses," guesses left")
      print("Available letters are",get_available_letters(letters_guessed))

      for i in letters_guessed:
        word_guess+=i
        word_guess.replace(' ','')
      user_guess=input("Guess a letter homie: ")
      if user_guess=='*':
        print("Possible words are", show_possible_matches(word_guess))
      warning=2
      print("You have", warning+1, "warnings left")
      while warning>0:
        if user_guess.isalpha()==False or len(user_guess)>1:
          warning-=1
          print("That ain't a letter, you got ",warning+1," warnings left")
          user_guess=input("Guess a letter homie: ")
        else:
            break
          
      if warning==0:
        no_of_guesses-=1
        print("you have", no_of_guesses, "guesses left")
      user_guess.lower()


      if user_guess in secret_word and user_guess not in letters_guessed:
        letters_guessed.append(user_guess)
        print("Ayeeeeee great guess homie: ", get_guessed_word(secret_word,letters_guessed))
      elif user_guess in letters_guessed:
        print("Damnnnn homie, you've guessed this one already: ", get_guessed_word(secret_word,letters_guessed))
      elif user_guess not in secret_word:
        print("Damnnnn homie, this letter ain't in ma word: ", get_guessed_word(secret_word,letters_guessed))
        letters_guessed.append(user_guess)
        no_of_guesses-=1
    if no_of_guesses==0:
      print('------------')
      print("Game Over")
      print("No guesses left")
      print("Loser oof")
      print("The correct word was ", secret_word)
      break
    else:
      continue





# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
  #secret_word = choose_word(wordlist)
  #hangman(secret_word)
  secret_word = choose_word(wordlist)
  hangman_with_hints(secret_word)
    

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    
    

import random
import string

WORDLIST_FILENAME = 'words.txt'

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    """

    print('Loading word list from file...')

    with open(WORDLIST_FILENAME, 'r') as in_file:
        line = in_file.readline()
        word_list = line.split()
        print('   ', len(word_list), 'words loaded.')
        return word_list

def choose_word(word_list):
    """
    word_list (list): list of words (strings)

    Returns a word from word_list at random
    """

    return random.choice(word_list)

wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in letters_guessed;
      False otherwise
    '''

    for letter in secret_word:
        if letter in letters_guessed:
            continue
        return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''

    word_guesssed = ''

    for letter in secret_word:
        if letter in letters_guessed:
            word_guesssed += letter
        else:
            word_guesssed += ' _ '

    return word_guesssed.upper()


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    letters_available = list(string.ascii_lowercase)

    for letter in letters_guessed:
        if letter in letters_available:
            letters_available.remove(letter)

    return ''.join(letters_available)

def play_new_game():
    """
    chooses a secret_word from the list
    and starts the game
    """

    secret_word = choose_word(wordlist).lower()
    hangman(secret_word)

def play_again():
    """
    Ask the user if they want to play again
    """

    next_game = input('Do you want to play again? yes/no: ').lower()

    if next_game == 'yes' or next_game == 'y':
        play_new_game()
    elif next_game == 'no' or next_game == 'n':
        exit()
    else:
        print("Your input is neither 'yes' nor 'no': ")
        print('')
        play_again()

def hangman(secret_word):

    letters_guessed = []
    guesses = 8

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is {} letters long. {}'.\
        format(len(secret_word), len(secret_word) * ' _ '))

    while not is_word_guessed(secret_word, letters_guessed):
        print('***')
        print('You have {} guesses left.'.format(guesses))
        print('Available letters: ', get_available_letters(letters_guessed))
        user_guess = input('Please guess a letter: ').lower()

        word_guesssed = get_guessed_word(secret_word, letters_guessed)

        if user_guess not in string.ascii_lowercase:
            print('Your guess is not a letter!', word_guesssed)

        elif len(user_guess) > 1:
            print('Guess only one letter!', word_guesssed)

        elif user_guess not in letters_guessed:
            letters_guessed.append(user_guess) 

            if user_guess in secret_word:
                print('Good guess: ', \
                    get_guessed_word(secret_word, letters_guessed))
            else:
                print('Oops! That letter is not in my word:', word_guesssed)
                guesses -= 1
        
        else:
            print("Oops! You've already guessed that letter:", word_guesssed)

        if guesses == 0:
            print('***')
            print('Sorry, you ran out of guesses. The word was {}.'.\
                format(secret_word.upper()))
            play_again()

    print('***')
    print('Congratulations, you won!')
    play_again()

play_new_game()
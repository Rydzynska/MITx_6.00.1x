import random
import string

"""
Scrabble game. Computer chooses a word, only the player guesses.
"""

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 10

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 
    'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 
    'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Return a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    in_file = open(WORDLIST_FILENAME, 'r')
    word_list = []
    for line in in_file:
        word_list.append(line.strip().lower())
    print("  ", len(word_list), "words loaded.")
    return word_list

def get_frequency_dict(sequence):
    """
    Return a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def get_word_score(word, n):
    """
    Return the score for a word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """    
    score = 0

    for letter in word:
        score += SCRABBLE_LETTER_VALUES.get(letter, 0)

    score *= len(word)

    if len(word) == n:
        score += 50

    return score     

def display_hand(hand):
    """
    Display the letters currently in the hand.
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")
    print()                             

def deal_hand(n):
    """
    Return a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    n: int >= 0
    return: dictionary (string -> int)
    """
    hand = {}
    num_vowels = n // 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

def update_hand(hand, word):
    """
    Assume that 'hand' has all the letters in word.
    Update the hand: use up the letters in the given word
    and return the new hand, without those letters in it.

    Do not modify hand.

    word: string
    hand: dictionary (string -> int)    
    return: dictionary (string -> int)
    """
    new_hand = dict(hand)

    for i in word:
        new_hand[i] -= 1

    return new_hand

def is_valid_word(word, hand, word_list):
    """
    Return True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Do not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    new_hand = dict(hand)

    if word in word_list:
        for letter in word:
            if new_hand.get(letter, 0) == 0:
                return False
            else:
                new_hand[letter] -= 1 
        return True
    return False

def calculate_hand_len(hand):
    """ 
    Return the length in the current hand.
    
    hand: dictionary (string-> int)
    return: integer
    """
    
    hand_len = 0

    for value in hand.values():
        hand_len += value

    return hand_len


def play_hand(hand, word_list, n):
    """
    Allow the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    total_score = 0

    while calculate_hand_len(hand) != 0:
        print("Current Hand: ", end='') 
        display_hand(hand)
        word = input('Enter word, or a "." to indicate that you are finished: ')
        if is_valid_word(word, hand, word_list) == False and word != ".":
            print("Invalid word, please try again.")
            print()
        elif is_valid_word(word, hand, word_list) == True:
            total_score += get_word_score(word, n)
            print('" {0} " earned {1}  points. Total:  {2}  points'
                .format(word, get_word_score(word, n), total_score))
            print()
            hand = update_hand(hand, word)
        else:
            print("Goodbye! Total score:  {}  points".format(total_score))
            break
    else:
        print("Run out of letters. Total score:  {}  points".format(total_score))

def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    1) Ask the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """

    hand = {}

    while True:
        user_input = input("Enter n to deal a new hand, r to replay the last "
                            "hand, or e to end game: ")
        print()
        if user_input == "n":
            hand = deal_hand(HAND_SIZE)
            play_hand(hand, word_list, HAND_SIZE)
        if user_input == "e":
            break
        if user_input == "r":
            if hand != {}:
                play_hand(hand, word_list, HAND_SIZE)
            else:
                print("You have not played a hand yet."
                      "Please play a new hand first!")
                print()
                play_game(word_list)
        if user_input not in ['n', 'e', 'r']:
            print("Invalid command.")
            play_game(word_list)


if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

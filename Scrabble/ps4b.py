from ps4a import *
import time

"""
Scrabble game. Computer plays against player.
"""

def comp_choose_word(hand, word_list, n):
    """
    Given a hand and a word_list, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    word_list: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    max_score = 0  
    best_word = None

    for word in word_list:
        if is_valid_word(word, hand, word_list) == True:
            score = get_word_score(word, n)
            if score > max_score:
                max_score = score
                best_word = word

    return best_word

def comp_play_hand(hand, word_list, n):
    """
    Allow the computer to play the given hand, following the same procedure
    as play_hand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. comp_choose_word returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    total_score = 0

    while calculate_hand_len(hand) != 0:
        print("Current Hand:", end='')
        display_hand(hand)

        word = comp_choose_word(hand, word_list, n)
        if word:
            total_score += get_word_score(word, n)
            print('"{0}" earned {1} points. Total: {2} points'
                .format(word, get_word_score(word, n), total_score))
            print()

            hand = update_hand(hand, word)
        else:
            print("Total score: {} points".format(total_score))
            print()
            break
    else:
        print("Run out of letters. Total score: {} points".format(total_score))
        print()

def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using play_hand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using comp_play_hand.

    4) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    
    hand = {}
    while True:
        user_input = input("Enter n to deal a new hand, "
                        "r to replay the last hand, or e to end game: ")
        if user_input == "n":
            hand = deal_hand(HAND_SIZE)
            player = input("Enter u to have yourself play, "
                        "c to have the computer play: ")
            if player == "u":
                play_hand(hand, word_list, HAND_SIZE)
            elif player == "c":
                comp_play_hand(hand, word_list, HAND_SIZE)
            else:
                print("Invalid command.")
                play_game(word_list)

        if user_input == "e":
            break
        if user_input == "r":
            if hand != {}:
                player = input("Enter u to have yourself play, "
                            "c to have the computer play: ")
                if player == "u":
                    play_hand(hand, word_list, HAND_SIZE)
                elif player == "c":
                    comp_play_hand(hand, word_list, HAND_SIZE)
                else:
                    print("Invalid command.")
                    play_game(word_list)     
            else:
                print("You have not played a hand yet. "
                    "Please play a new hand first!")
                print
                play_game(word_list)

        if user_input not in ['n', 'e', 'r']:
            print("Invalid command.")
            play_game(word_list)

if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)




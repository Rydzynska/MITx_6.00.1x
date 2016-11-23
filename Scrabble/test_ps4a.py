from ps4a import *

def test_get_word_score():
    failure=False
    words = {("", 7):0, ("it", 7):4, ("was", 7):18, ("scored", 7):54, 
            ("waybill", 7):155, ("outgnaw", 7):127, 
            ("fork", 7):44, ("fork", 4):94}

    for (word, n) in words.keys():
        score = get_word_score(word, n)
        if score != words[(word, n)]:
            print("FAILURE: test_get_word_score()")
            print("\tExpected", words[(word, n)], "points but got '" 
                    + str(score) + "' for word '" + word 
                    + "', n=" + str(n))
            failure=True
    if not failure:
        print("SUCCESS: test_get_word_score()")

def test_is_valid_word(word_list):
    failure=False
    # test 1
    word = "hello"
    hand_origin = get_frequency_dict(word)
    hand_copy = hand_origin.copy()

    if not is_valid_word(word, hand_copy, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '" 
                + word + "' and hand:", hand_origin)

        failure = True

    # Test a second time to see if wordList or hand has been modified
    if not is_valid_word(word, hand_copy, word_list):
        print("FAILURE: test_is_valid_word()")

        if hand_copy != hand_origin:
            print("\tTesting word", word, "for a second time")
            print("\tAt this point, hand ought to be", hand_origin,
                    "but it is", hand_copy)

        else:
            print("\tTesting word", word, "for a second time")
            word_in_word_list = word in word_list
            print("The word", word, "should be in word_list", 
                    word_in_word_list)

        print("\tExpected True, but got False for word: '" + word 
                + "' and hand:", hand_copy)

        failure = True


    # test 2
    hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
    word = "rapture"

    if  is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word 
            + "' and hand:", hand)

        failure = True        

    # test 3
    hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "honey"

    if  not is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '"+ word 
                +"' and hand:", hand)

        failure = True                        

    # test 4
    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
    word = "honey"

    if  is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word 
                + "' and hand:", hand)
        
        failure = True

    # test 5
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = "evil"
    
    if  not is_valid_word(word, hand, word_list):
        print("FAILURE: test_isValidWord()")
        print("\tExpected True, but got False for word: '" + word 
            + "' and hand:", hand)
        
        failure = True
        
    # test 6
    word = "even"

    if  is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word 
                + "' and hand:", hand)        
        
        failure = True        

    if not failure:
        print("SUCCESS: test_is_valid_word()")


word_list = load_words()
print("--------------------------------------------------------------------")
print("Testing get_word_score...")
test_get_word_score()
print("--------------------------------------------------------------------")
print("Testing is_valid_word...")
test_is_valid_word(word_list)
print("--------------------------------------------------------------------")
print("All done!")

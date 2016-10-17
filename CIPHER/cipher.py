text = "story.txt"

def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Return a list of valid words. Words are strings of lowercase letters.
    '''
    print('Loading word list from file...')

    with open(file_name, 'r') as in_file:
        line = in_file.readline()
        word_list = line.split()
        print('  ', len(word_list), 'words loaded.\n')

    return word_list

def is_word(word_list, word):
    '''
    Determine if word is a valid word, ignoring
    capitalization and punctuation
 
    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Return True if word is in word_list, False otherwise
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"\n")
    return word in word_list

def get_story_string():
    """
    Return a text written in a chosen file in encrypted text.
    """
    with open(text, "r") as f_text:
        story = str(f_text.read())
        return story

WORDLIST_FILENAME = 'words.txt'


class Message():
    def __init__(self, text):
        '''
        Initialize a Message object
                
        text (string): the message's text
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        return self.valid_words.copy()
        
    def build_shift_dict(self, shift):
        '''
        Create a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift.       
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Return a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        cipher = {}

        for letter in alphabet:
            cipher[letter] = alphabet[shift]
            cipher[letter.upper()] = alphabet.upper()[shift]
            
            if shift < len(alphabet) - 1:
                shift += 1
            else:
                shift = 0

        return cipher

    def apply_shift(self, shift):
        '''
        Apply the Caesar Cipher to self.message_text with the input shift.
        Create a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Return the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''

        new_text = ""
        cipher = self.build_shift_dict(shift)

        for letter in self.message_text:
            new_text += cipher.get(letter, letter)

        return new_text


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initialize a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''

        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)
        
    def get_shift(self):
        return self.shift

    def get_encrypting_dict(self):
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Change self.shift of the PlaintextMessage and update other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Return nothing
        '''

        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initialize a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one (i.e. creates the maximum number of real words)

        Return a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        best_match = 0
        best_shift = 0
        best_text = ""

        for shift in range(1, 27):
            decrypted_text = Message.apply_shift(self, 26 - shift)
            decrypted_words = decrypted_text.split(' ')

            counter = 0

            for word in decrypted_words:
                if is_word(self.valid_words, word):
                    counter += 1

            if counter > best_match:
                best_match = counter
                best_shift = 26 - shift
                best_text = decrypted_text
                
        return (best_shift, best_text)


def decrypt_story():
    story = get_story_string()
    decrypted_story = CiphertextMessage(story)

    return decrypted_story.decrypt_message()


if __name__ == '__main__':
    print(decrypt_story())
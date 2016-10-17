import unittest
import cipher

class TestIsWord(unittest.TestCase):
    def test_is_word1(self):
        self.assertTrue(
            cipher.is_word(['arks', 'arms', 'army', 'arts', 'asks'], 'asks')
            )

    def test_is_word2(self):
        self.assertFalse(
            cipher.is_word(['arks', 'arms', 'army', 'arts', 'asks'], 'anew')
            )



class TestEncryptMessage(unittest.TestCase):
    def test_encrypt_msg_shift_1(self):
        self.plaintext = cipher.PlaintextMessage('earth', 1)
        self.assertEqual(
            self.plaintext.get_message_text_encrypted(), 'fbsui')

    def test_encrypt_msg_shift_3(self):
        self.plaintext = cipher.PlaintextMessage('cat', 3)
        self.assertEqual(
            self.plaintext.get_message_text_encrypted(), 'fdw')

    def test_encrypt_msg_shift_5(self):
        self.plaintext = cipher.PlaintextMessage('apple', 5)
        self.assertEqual(
            self.plaintext.get_message_text_encrypted(), 'fuuqj')

    def test_encrypt_msg_shift_7(self):
        self.plaintext = cipher.PlaintextMessage('worm', 7)
        self.assertEqual(
            self.plaintext.get_message_text_encrypted(), 'dvyt')

    def test_encrypt_msg_shift_9(self):
        self.plaintext = cipher.PlaintextMessage('rose', 9)
        self.assertEqual(
            self.plaintext.get_message_text_encrypted(), 'axbn')

    def test_encrypt_msg_shift_11(self):
        self.plaintext = cipher.PlaintextMessage('wardrobe', 11)
        self.assertEqual(
            self.plaintext.get_message_text_encrypted(), 'hlcoczmp')

    def test_encrypt_msg_shift_13(self):
        self.plaintext = cipher.PlaintextMessage('shirt', 13)
        self.assertEqual(
            self.plaintext.get_message_text_encrypted(), 'fuveg')

    def test_encrypt_msg_shift_15(self):
        self.plaintext = cipher.PlaintextMessage('rope', 15)
        self.assertEqual(
            self.plaintext.get_message_text_encrypted(), 'gdet')

    def test_encrypt_msg_shift_17(self):
        self.plaintext = cipher.PlaintextMessage('baguette', 17)
        self.assertEqual(
            self.plaintext.get_message_text_encrypted(), 'srxlvkkv')

    def test_encrypt_msg_shift_19(self):
        self.plaintext = cipher.PlaintextMessage('carpet', 19)
        self.assertEqual(
            self.plaintext.get_message_text_encrypted(), 'vtkixm')

    def test_encrypt_msg_shift_21(self):
        self.plaintext = cipher.PlaintextMessage('duvet', 21)
        self.assertEqual(
            self.plaintext.get_message_text_encrypted(), 'ypqzo')

    def test_encrypt_msg_shift_23(self):
        self.plaintext = cipher.PlaintextMessage('juice', 23)
        self.assertEqual(
            self.plaintext.get_message_text_encrypted(), 'grfzb')

    def test_encrypt_msg_shift_25(self):
        self.plaintext = cipher.PlaintextMessage('blueberry', 25)
        self.assertEqual(
            self.plaintext.get_message_text_encrypted(), 'aktdadqqx')

    def test_encrypt_msg_with_capital_letters(self):
        self.plaintext = cipher.PlaintextMessage('BluEbErRy', 25)
        self.assertEqual(
            self.plaintext.get_message_text_encrypted(), 'AktDaDqQx')

    def test_encrypt_msg_with_number(self):
        self.plaintext = cipher.PlaintextMessage('5 carpet', 19)
        self.assertEqual(
            self.plaintext.get_message_text_encrypted(), '5 vtkixm')



class TestDescryptMessage(unittest.TestCase):
    def test_descrypt_msg_shift2(self):
        self.ciphertext = cipher.CiphertextMessage("pybgm")
        self.assertEqual(
            self.ciphertext.decrypt_message(), (2, "radio"))

    def test_descrypt_msg_shift4(self):
        self.ciphertext = cipher.CiphertextMessage("jkjoajoa")
        self.assertEqual(
            self.ciphertext.decrypt_message(), (4, "nonsense"))

    def test_descrypt_msg_shift6(self):
        self.ciphertext = cipher.CiphertextMessage("giomy")
        self.assertEqual(
            self.ciphertext.decrypt_message(), (6, "mouse"))

    def test_descrypt_msg_shift8(self):
        self.ciphertext = cipher.CiphertextMessage("xslzwj")
        self.assertEqual(
            self.ciphertext.decrypt_message(), (8, "father"))
            
    def test_descrypt_msg_shift10(self):
        self.ciphertext = cipher.CiphertextMessage("sxysaud")
        self.assertEqual(
            self.ciphertext.decrypt_message(), (10, "chicken"))

    def test_descrypt_msg_shift12(self):
        self.ciphertext = cipher.CiphertextMessage("ghfok")
        self.assertEqual(
            self.ciphertext.decrypt_message(), (12, "straw"))

    def test_descrypt_msg_shift14(self):
        self.ciphertext = cipher.CiphertextMessage("oaybgfqd")
        self.assertEqual(
            self.ciphertext.decrypt_message(), (14, "computer"))

    def test_descrypt_msg_shift16(self):
        self.ciphertext = cipher.CiphertextMessage("mrksb")
        self.assertEqual(
            self.ciphertext.decrypt_message(), (16, "chair"))

    def test_descrypt_msg_shift18(self):
        self.ciphertext = cipher.CiphertextMessage("aqabmz")
        self.assertEqual(
            self.ciphertext.decrypt_message(), (18, "sister"))

    def test_descrypt_msg_shift20(self):
        self.ciphertext = cipher.CiphertextMessage("hgriute")
        self.assertEqual(
            self.ciphertext.decrypt_message(), (20, "balcony"))

    def test_descrypt_msg_shift22(self):
        self.ciphertext = cipher.CiphertextMessage("nierw")
        self.assertEqual(
            self.ciphertext.decrypt_message(), (22, "jeans"))

    def test_descrypt_msg_shift24(self):
        self.ciphertext = cipher.CiphertextMessage("wpkxgtukva")
        self.assertEqual(
            self.ciphertext.decrypt_message(), (24, "university"))

    def test_descrypt_msg_with_capital_letters(self):
        self.ciphertext = cipher.CiphertextMessage("GiOmY")
        self.assertEqual(
            self.ciphertext.decrypt_message(), (6, "MoUsE"))

    def test_descrypt_msg_with_number(self):
        self.ciphertext = cipher.CiphertextMessage("hgriute 10")
        self.assertEqual(
            self.ciphertext.decrypt_message(), (20, "balcony 10"))

    def test_encrypt_decrypt_sentence_with_punctuation(self):
        self.plaintext = cipher.PlaintextMessage('Cat, dog@,  .', 19)
        encrypted_text = self.plaintext.get_message_text_encrypted()

        self.ciphertext = cipher.CiphertextMessage(encrypted_text)
        self.assertEqual(
            self.ciphertext.decrypt_message(), (7, 'Cat, dog@,  .'))



if __name__ == '__main__':
   unittest.main()
import unittest
from encryption.aes_encryption import encrypt_message, decrypt_message

class TestEncryption(unittest.TestCase):
    
    def test_encryption_decryption(self):
        key = "thisisaverysecret"
        message = "Test message"
        
        encrypted_message = encrypt_message(message, key)
        decrypted_message = decrypt_message(encrypted_message, key)
        
        self.assertEqual(message, decrypted_message)

if __name__ == "__main__":
    unittest.main()

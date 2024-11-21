import unittest
from qr_code.generate_qr import generate_qr_code
from qr_code.decode_qr import decode_qr_code

class TestQRCode(unittest.TestCase):

    def test_qr_code_generation(self):
        message = "Test QR message"
        qr_image_path = generate_qr_code(message)
        self.assertTrue(qr_image_path.endswith('.png'))

    def test_qr_code_decoding(self):
        qr_image_path = "encrypted_qr.png"
        decoded_message = decode_qr_code(qr_image_path)
        self.assertIsNotNone(decoded_message)

if __name__ == "__main__":
    unittest.main()

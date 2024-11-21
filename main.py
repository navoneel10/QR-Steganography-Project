from src.encryption.aes_encryption import encrypt_message, decrypt_message
from src.qr_code.generate_qr import generate_qr_code
from src.qr_code.decode_qr import decode_qr_code
from src.steganography.embed import embed_message
from src.steganography.extract import extract_message
from utils.logger import setup_logger

def main():
    logger = setup_logger()
    
    print("Welcome to the Steganography QR Code Project!")
    print("1. Encrypt and embed message in QR code")
    print("2. Decode QR code and decrypt message")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        message = input("Enter the message to encrypt: ")
        key = input("Enter encryption key (16 bytes for AES): ")
        
        # Encrypt the message
        encrypted_message = encrypt_message(message, key)
        print(f"Encrypted message: {encrypted_message}")
        
        # Embed the encrypted message in a QR code
        qr_image_path = generate_qr_code(encrypted_message)
        print(f"QR code saved at: {qr_image_path}")
    
    elif choice == '2':
        file_path = input("Enter the path of the QR code to decode: ")
        key = input("Enter decryption key: ")
        
        # Decode the QR code and extract the encrypted message
        encrypted_message_from_qr = decode_qr_code(file_path)
        print(f"Extracted Encrypted Message: {encrypted_message_from_qr}")
        
        # Decrypt the message
        decrypted_message = decrypt_message(encrypted_message_from_qr, key)
        print(f"Decrypted message: {decrypted_message}")
    
    else:
        print("Invalid choice! Exiting.")
    
if __name__ == "__main__":
    main()

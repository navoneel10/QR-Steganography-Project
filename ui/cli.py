import sys
import os

# Add the 'src' directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from encryption.aes_encryption import encrypt_message, decrypt_message
from qr_code.generate_qr import generate_qr_code
from qr_code.decode_qr import decode_qr_code

def print_welcome():
    """Display the welcome message and options to the user."""
    print("\nWelcome to the Steganography QR Code Project!")
    print("Select an option:")
    print("1. Encrypt and embed a message in QR code")
    print("2. Decode QR code and decrypt the message")
    print("3. Exit")

def get_valid_key(prompt):
    """Prompt the user for a valid 16-byte AES encryption key."""
    while True:
        key = input(prompt)
        if len(key) == 16:
            return key
        else:
            print("Error: The AES key must be exactly 16 bytes. Please try again.")

def encrypt_and_embed():
    """Encrypt the message and embed it in a QR code."""
    message = input("Enter the message to encrypt: ")

    # Get a valid 16-byte AES key
    key = get_valid_key("Enter encryption key (16 bytes for AES): ")

    try:
        # Encrypt the message
        encrypted_message = encrypt_message(message, key)
        print(f"\nEncrypted message: {encrypted_message}")

        # Embed the encrypted message in a QR code
        qr_image_path = generate_qr_code(encrypted_message)
        print(f"\nQR code saved at: {qr_image_path}")
    except Exception as e:
        print(f"Error during encryption or QR code generation: {e}")

def decode_and_decrypt():
    """Decode a QR code and decrypt the message."""
    file_path = input("Enter the path of the QR code to decode: ")

    # Check if the file exists
    if not os.path.isfile(file_path):
        print("Error: File not found. Please check the file path and try again.")
        return

    key = get_valid_key("Enter decryption key: ")

    try:
        # Decode the QR code and extract the encrypted message
        encrypted_message_from_qr = decode_qr_code(file_path)
        if encrypted_message_from_qr:
            print(f"\nExtracted Encrypted Message: {encrypted_message_from_qr}")

            # Decrypt the message
            decrypted_message = decrypt_message(encrypted_message_from_qr, key)
            print(f"\nDecrypted message: {decrypted_message}")
        else:
            print("Error: Could not extract a message from the QR code.")
    except Exception as e:
        print(f"Error during decryption: {e}")

def main():
    """Main function to run the program."""
    while True:
        print_welcome()
        choice = input("Enter your choice: ")

        if choice == '1':
            encrypt_and_embed()
        elif choice == '2':
            decode_and_decrypt()
        elif choice == '3':
            print("Exiting the program...")
            sys.exit(0)  # Exit the program gracefully
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
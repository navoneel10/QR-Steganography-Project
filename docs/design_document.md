# Design Document for Steganography QR Code Project

## Table of Contents
1. [Introduction](#introduction)
2. [System Architecture](#system-architecture)
3. [Modules and Components](#modules-and-components)
    - [Encryption Module](#encryption-module)
    - [QR Code Generation Module](#qr-code-generation-module)
    - [Steganography Module](#steganography-module)
    - [CLI Interface](#cli-interface)
4. [Data Flow](#data-flow)
5. [Security Considerations](#security-considerations)
6. [Error Handling](#error-handling)
7. [Testing Strategy](#testing-strategy)
8. [Future Work and Enhancements](#future-work-and-enhancements)

---

## 1. Introduction

The Steganography QR Code project aims to combine AES encryption with QR code generation to provide a secure method for transmitting encrypted messages. The project is designed to allow users to encrypt messages, embed them in QR codes, and later decode and decrypt the messages using a secret key.

---

## 2. System Architecture

The architecture of the Steganography QR Code system follows a modular design, with clear separation of concerns:

- **Encryption Module**: Handles encryption and decryption using AES.
- **QR Code Generation**: Generates a QR code from an encrypted message.
- **Steganography Module**: Embeds the encrypted message in the QR code and extracts it later.
- **User Interface**: A command-line interface (CLI) for users to interact with the system.

---

## 3. Modules and Components

### **Encryption Module**
- **Functionality**: Encrypts and decrypts messages using AES in CBC mode.
- **Libraries**: `pycryptodome`
- **Key Management**: AES key must be 16 bytes long.
- **Methods**:
    - `encrypt_message(message, key)`: Encrypts a given message using the provided key.
    - `decrypt_message(encrypted_message, key)`: Decrypts the encrypted message using the provided key.

### **QR Code Generation Module**
- **Functionality**: Generates QR codes from text input.
- **Libraries**: `qrcode`
- **Methods**:
    - `generate_qr_code(message)`: Generates and saves a QR code image containing the provided message.

### **Steganography Module**
- **Functionality**: Embeds and extracts messages in QR codes.
- **Libraries**: `opencv-python`
- **Methods**:
    - `embed_message(qr_image, encrypted_message)`: Embeds the encrypted message into the QR code.
    - `extract_message(qr_image)`: Extracts the hidden message from the QR code.

### **CLI Interface**
- **Functionality**: Allows the user to interact with the system via a command-line interface.
- **Methods**:
    - User selects an option (Encrypt and embed or Decode and decrypt).
    - The program calls the appropriate methods based on user input.
  
---

## 4. Data Flow

1. **Encryption and Embedding**:
    - User inputs a message and encryption key.
    - The message is encrypted using the AES algorithm.
    - The encrypted message is embedded into a QR code.
    - The QR code is saved as an image.

2. **Decoding and Decrypting**:
    - User provides a QR code image and decryption key.
    - The QR code is decoded to extract the encrypted message.
    - The extracted message is decrypted using the provided key.

---

## 5. Security Considerations

- **Key Management**: It is important that the encryption key is kept secure. If the key is compromised, the encrypted messages can be decrypted.
- **AES Encryption**: AES is a strong encryption algorithm, but proper key management is crucial to the overall security of the system.
- **QR Code Security**: While QR codes themselves are not inherently insecure, the hidden message may be vulnerable to reverse engineering if the key is compromised.

---

## 6. Error Handling

- **Invalid Key**: If an incorrect key is provided during decryption, the system will return an error message indicating that the decryption failed.
- **Corrupted QR Code**: If the QR code is damaged or invalid, the system will notify the user that the QR code could not be decoded.
- **Invalid Input**: The system checks for valid inputs, such as the message to be encrypted, ensuring that they meet the required format.

---

## 7. Testing Strategy

- **Unit Tests**: Each module (encryption, QR code generation, steganography) will have unit tests to verify individual functionality.
- **Integration Testing**: Ensure that the encryption and embedding processes work together correctly.
- **UI Testing**: Manual testing of the CLI interface to verify the user experience.

---

## 8. Future Work and Enhancements

- **Web Interface**: Develop a web-based interface for easier user interaction.
- **Mobile App**: Create a mobile application to enable QR code encryption and decryption on mobile devices.
- **Advanced Encryption**: Explore using RSA or ECC for key exchange and message encryption.

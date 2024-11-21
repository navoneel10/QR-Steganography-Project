# User Manual for Steganography QR Code Project

## Table of Contents
1. [Introduction](#introduction)
2. [System Requirements](#system-requirements)
3. [Installation Instructions](#installation-instructions)
4. [How to Use](#how-to-use)
    - [Encrypt and Embed Message in QR Code](#encrypt-and-embed-message-in-qr-code)
    - [Decode QR Code and Decrypt Message](#decode-qr-code-and-decrypt-message)
5. [Troubleshooting](#troubleshooting)
6. [Contact Information](#contact-information)

---

## 1. Introduction

Welcome to the Steganography QR Code Project! This project allows users to encrypt messages and embed them in QR codes, or decode QR codes and decrypt the embedded messages. The encryption is performed using AES (Advanced Encryption Standard) in CBC mode, ensuring secure communication.

---

## 2. System Requirements

- **Operating System**: Windows, Linux, or macOS
- **Python Version**: 3.7 or higher
- **Required Libraries**:
  - `pycryptodome`
  - `qrcode`
  - `opencv-python`
  
---

## 3. Installation Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/QR-Steganography-Project.git
   cd QR-Steganography-Project

2. **Install Dependencies: Install the required libraries using pip**:
   ```bash
    pip install -r requirements.txt

3. **Run the Application: To run the command-line interface (CLI), use**:
   ```bash
   python ui/cli.py

## 4. How to Use
### Encrypt and Embed Message in QR Code

1. **Run the application using the CLI**:
   ```bash
   python ui/cli.py

### Encrypt and Embed Message in QR Code

1. Select option **1** to encrypt and embed a message.
2. Enter the message you want to encrypt.
3. Enter a **16-byte AES encryption key** (e.g., `password12345678`).
4. The program will display the encrypted message and save the QR code image at a specified location.

### Decode QR Code and Decrypt Message

1. Select option **2** to decode a QR code and decrypt the message.
2. Enter the file path of the QR code image you want to decode.
3. Enter the **decryption key** used when the message was encrypted.
4. The program will display the decrypted message.

### 5. Troubleshooting

- **Error: "Invalid Key"**: Ensure that the correct decryption key is used. AES encryption requires an exact key for successful decryption.
- **Error: "Invalid QR Code"**: Check if the QR code is corrupted or the message was not properly embedded.

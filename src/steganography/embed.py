# Embed the encrypted message into the QR code image (used in generate_qr.py)

def embed_message(qr, encrypted_message):
    # This function is implemented as part of the QR code generation
    # Here you could add an additional layer of embedding logic if necessary
    return qr.add_data(encrypted_message)

import qrcode

def generate_qr_code(encrypted_message):
    qr = qrcode.QRCode(
        version=1,  # QR code version
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box
        border=4,  # Border thickness
    )
    qr.add_data(encrypted_message)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img_path = "encrypted_qr.png"
    img.save(img_path)
    return img_path

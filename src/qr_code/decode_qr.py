import cv2

def decode_qr_code(file_path):
    # Initialize the QRCodeDetector
    detector = cv2.QRCodeDetector()

    # Read the image from the given file path
    img = cv2.imread(file_path)

    # Use the detectAndDecode method to detect and decode the QR code
    value, pts, qr_code = detector.detectAndDecode(img)

    # Check if QR code was successfully detected
    if value:
        return value  # Return the decoded string
    else:
        print("QR code could not be decoded.")
        return None

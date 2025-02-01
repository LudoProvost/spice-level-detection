import cv2

def read_qr_code(cap):
    """Open the camera, look for a QR code, and return the data from the QR code."""
    
    detector = cv2.QRCodeDetector()
    
    if not cap.isOpened():
        raise RuntimeError("Error: Could not open webcam.")

    ret, frame = cap.read()
    if not ret:
        # cap.release()
        raise RuntimeError("Error: Could not read frame.")

    # Detect and decode QR code
    data, vertices_array, _ = detector.detectAndDecode(frame)

    # cap.release()
    # cv2.destroyAllWindows()
    return data 
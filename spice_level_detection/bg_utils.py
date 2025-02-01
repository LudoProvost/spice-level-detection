import cv2
from .bound_box import BoundBox

def get_empty_bg(cap, bound_box: BoundBox, output_path="ref-bg.jpg", imwrite=False):
    """Capture a frame from the webcam and save the cropped region as the reference background image."""

    if not cap.isOpened():
        raise RuntimeError("Error: Could not open webcam.")

    ret, frame = cap.read()
    if not ret:
        # cap.release()
        raise RuntimeError("Error: Could not read frame.")

    cropped_frame = frame[bound_box.y1:bound_box.y2, bound_box.x1:bound_box.x2]
    
    if (imwrite):
        cv2.imwrite(output_path, cropped_frame)

    # cap.release()
    # cv2.destroyAllWindows()
    return cropped_frame
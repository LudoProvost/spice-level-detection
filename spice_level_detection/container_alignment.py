import cv2
import numpy as np
from .bound_box import BoundBox

def get_alignment(cap, reference_image_path="ref-bg.jpg", getBoundBox=False):
    """
    Finds the best matching location of the reference image in the frame using template matching.
    Returns the dx and dy between the center of the frame and the center of the best match.

    Returns:
    - tuple: (dx, dy) - IF getBoundBox = False. The difference between the center of the frame and the center of the best match.
    - BoundBox: The bounding box of the best match - IF getBoundBox = True.
    """
    
    reference_image = cv2.imread(reference_image_path)
    if reference_image is None:
        raise RuntimeError(f"Error: Could not read reference image from {reference_image_path}")

    if not cap.isOpened():
        raise RuntimeError("Error: Could not open webcam.")

    ret, frame = cap.read()
    if not ret:
        # cap.release()
        raise RuntimeError("Error: Could not read frame.")

    # Convert the reference image and frame to grayscale
    ref_gray = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Get dimensions of the reference image
    h, w = ref_gray.shape

    # Apply template matching
    result = cv2.matchTemplate(frame_gray, ref_gray, cv2.TM_CCOEFF_NORMED)

    # Find the best match location
    _, _, _, max_loc = cv2.minMaxLoc(result)
    best_x, best_y = max_loc

    # Calculate the center of the detected region (best match location)
    match_center_x = best_x + w // 2
    match_center_y = best_y + h // 2

    # Get the center of the frame
    frame_height, frame_width, _ = frame.shape
    frame_center_x = frame_width // 2
    frame_center_y = frame_height // 2

    # Compute dx and dy (difference between frame center and match center)
    dx = match_center_x - frame_center_x
    dy = match_center_y - frame_center_y

    if (getBoundBox):
        return BoundBox(best_x, best_y, best_x + w, best_y + h)
    else:
        return dx, dy
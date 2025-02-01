import cv2
import numpy as np
from .bound_box import BoundBox

def get_spice_level(bound_box: BoundBox, reference_image_path="ref-bg.jpg", threshold=45, density_threshold=40):
    """Calculate the spice level percentage based on the difference between the current frame and the reference image."""
    reference_image = cv2.imread(reference_image_path)
    if reference_image is None:
        raise RuntimeError(f"Error: Could not read reference image from {reference_image_path}")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Error: Could not open webcam.")

    ret, frame = cap.read()
    if not ret:
        cap.release()
        raise RuntimeError("Error: Could not read frame.")

    roi = frame[bound_box.y1:bound_box.y2, bound_box.x1:bound_box.x2]
    diff_red = cv2.absdiff(roi[:, :, 2], reference_image[:, :, 2])
    diff_green = cv2.absdiff(roi[:, :, 1], reference_image[:, :, 1])

    mask_red = diff_red >= threshold
    mask_green = diff_green >= threshold
    mask = np.logical_or(mask_red, mask_green).astype(np.uint8)

    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=2)

    green_density = np.sum(mask, axis=1) / mask.shape[1]

    top_y = None
    for i, density in enumerate(green_density):
        if density > density_threshold / 100:
            top_y = bound_box.y1 + i
            break

    cap.release()
    cv2.destroyAllWindows()

    if top_y is not None:
        percentage_position = (bound_box.y2 - top_y) / (bound_box.y2 - bound_box.y1) * 100
        return int(percentage_position)
    else:
        return 0
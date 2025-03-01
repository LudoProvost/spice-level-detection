import cv2

def rotate_image(frame, direction):
    """
    Rotates the input image (frame) either clockwise ('cw') or counterclockwise ('ccw') by 90 degrees.

    Args:
    - frame (ndarray): The image to rotate.
    - direction (str): The direction to rotate ('cw' for clockwise, 'ccw' for counterclockwise).

    Returns:
    - rotated_frame (ndarray): The rotated image.
    """
    if direction == 'cw':
        rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    elif direction == 'ccw':
        rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    else:
        raise ValueError("Direction must be either 'cw' or 'ccw'")

    return rotated_frame

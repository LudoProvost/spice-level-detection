# Spice Level Detection

A library to detect spice level in a frame using edge detection.

## Installation
To install the package, use pip:

```sh
 py -m pip index versions --index-url https://test.pypi.org/simple/ spice_level_detection
```

If you want to change the version:

```sh
py -m pip install --index-url https://test.pypi.org/simple/ --no-deps --upgrade --no-cache-dir spice_level_detection==<INSERT REQUIRED VERSION>
```

## Dependencies

- opencv-python
- numpy

## Functions

### get_spice_level
Calculate the spice level percentage based on the difference between the current frame and the reference image.

#### Parameters:
- cap: cv2.VideoCapture object
- bound_box: BoundBox object defining the region of interest
- reference_image_path: Path to the reference image
- threshold: Threshold for detecting differences in color channels
- density_threshold: Density threshold for determining spice level

#### Returns:
- int: Spice level percentage

#### Function implementation:
```python
def get_spice_level(cap, bound_box: BoundBox, reference_image_path="ref-bg.jpg", threshold=45, density_threshold=40) -> int:
```

### get_empty_bg
Capture a frame from the webcam and save the cropped region as the reference background image.

#### Parameters:
- cap: cv2.VideoCapture object
- bound_box: BoundBox object defining the region of interest
- output_path: Path to save the reference background image
- imwrite: Boolean flag to save the image to the output path

#### Returns:
- np.ndarray: Cropped frame

#### Function implementation:
```python
def get_empty_bg(cap, bound_box: BoundBox, output_path="ref-bg.jpg", imwrite=False) -> np.ndarray:
```

### read_qr_code
Look for a QR code in the video capture and return the data from the QR code. Returns an empty string if no QR code is found.

#### Parameters:
- cap: cv2.VideoCapture object

#### Returns:
- str: Data from the QR code

#### Function implementation:
```python
def read_qr_code(cap) -> str:
```

### BoundBox
A class to represent a bounding box.

#### Attributes:
- x1: int, x-coordinate of the top-left corner
- y1: int, y-coordinate of the top-left corner
- x2: int, x-coordinate of the bottom-right corner
- y2: int, y-coordinate of the bottom-right corner

## Example Usage

```python
import cv2
from spice_level_detection import get_spice_level, get_empty_bg, read_qr_code, BoundBox

# Initialize video capture
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("Error: Could not open webcam.")

# Define bounding box
bound_box = BoundBox(70, 25, 386, 369)

# Get spice level
spice_level = get_spice_level(cap, bound_box)
print(f"Spice Level: {spice_level}%")

# Get empty background
empty_bg = get_empty_bg(cap, bound_box, imwrite=True)
print("Empty background captured and saved.")

# Read QR code
qr_data = read_qr_code(cap)
print(f"QR Code Data: {qr_data}")

# Release video capture
cap.release()
cv2.destroyAllWindows()
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

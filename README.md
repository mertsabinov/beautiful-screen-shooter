# Image Viewer with Border and Gradient Background

## Usage

1. Run the script using the command line or an IDE
2. A GUI window will appear, click on the "Open Image" button
3. Select an image file and click "Open"
4. Enter the desired border size in the input box
5. The image will be displayed with a border and gradient background, and also saved as "screenshot_with_border_and_gradient.png"

## Technical Details

- The script uses PyQt5 for the GUI and PIL for image processing
- The border is added by drawing a rectangle with the desired size and color around the image
- The gradient background is created by generating a grayscale image and then colorizing it
- The resulting image with the border and gradient background is saved as "screenshot_with_border_and_gradient.png"

## Requirements

- Python 3
- PyQt5
- PIL (Pillow)

## Installation

1. Install Python 3
2. Install PyQt5 by running `pip install PyQt5`
3. Install PIL by running `pip install Pillow`
4. Clone or download this repository
5. Navigate to the repository and run the script with `python filename.py`

## Note

- Make sure to replace "filename" with the actual name of the script file.
- The border size should be entered as an integer.
- The gradient background color can be changed by modifying the RGB values in the code.

## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.

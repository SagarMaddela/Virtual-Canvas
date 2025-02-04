
# Virtual Canvas

## Overview
Virtual Canvas is an interactive drawing application that allows users to draw using hand gestures. Utilizing **MediaPipe** for hand tracking, this project enables gesture-based drawing, erasing, and shape selection using a webcam. The application provides an intuitive and touch-free way to create digital sketches.

## Features
- **Hand Tracking**: Uses **MediaPipe Hands** to detect and track hand movements.
- **Gesture-Based Drawing**: Supports freehand drawing, shape selection, and erasing.
- **Multiple Colors & Shapes**: Users can switch between different colors and shapes such as circles, rectangles, and ellipses.
- **Dynamic Brush & Eraser Thickness**: Adjusts based on finger distance.
- **Real-time Processing**: Smooth interaction and minimal latency.

## Technologies Used
- Python
- OpenCV
- MediaPipe
- NumPy
- os (for managing images and assets)

## Installation
1. **Clone the Repository**
   ```sh
   git clone https://github.com/SagarMaddela/Virtual-Canvas.git
   cd Virtual-Canvas
   ```

2. **Install Dependencies**
   Ensure you have Python installed (preferably 3.7+), then install the required packages:
   ```sh
   pip install opencv-python mediapipe numpy
   ```

## Usage
1. **Run the Application**
   ```sh
   python Main.py
   ```
2. **Interact Using Gestures**
   - **Index & Middle Finger Up** → Selection Mode (Choose colors/shapes/eraser)
   - **Only Index Finger Up** → Drawing Mode (Draw on the canvas)
   - **Index & Thumb Close Together** → Adjust Brush/Eraser Size

## Project Structure
```
VirtualCanvas/
│-- MY Header/          # Folder containing UI overlay images
│-- Main.py             # Main script to run the Virtual Canvas
│-- HandTrackingModule.py  # Module for hand tracking functionalities
│-- README.md           # Project documentation
```

## Troubleshooting
- **Camera Not Opening?**
  - Ensure your webcam is connected and functional.
  - Try changing `video = cv2.VideoCapture(1)` to `cv2.VideoCapture(0)`.

- **Hand Not Detected?**
  - Make sure your hand is well-lit and visible to the camera.
  - Adjust `detectionCon` in `handDetector()` for better recognition.

## Contributing
Feel free to fork this repository and submit pull requests for improvements.

## License
This project is open-source and available under the [Apache License](LICENSE).

## Author
Developed by **Sagar Maddela**

For any queries, feel free to reach out on GitHub.

---
**Happy Drawing! 🎨**


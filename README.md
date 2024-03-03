# Real-time Ball Tracking System

## Overview

This computer vision project focuses on real-time ball tracking using a webcam. The system allows users to track a ball of a specific color, providing continuous updates on its X and Y coordinates, as well as the area, in real-time. The project leverages CVZONE and OpenCV for computer vision tasks, utilizing contour detection to identify and extract center coordinates and area of the largest contour.

## Features

- **Color-Based Tracking:** Track a ball of a specific color using the webcam.
  
- **Interactive Setup:** Use `ball_setup.py` to set the color of the ball by adjusting Hue, Saturation, and Value (HSV) parameters interactively.

- **Real-time Feedback:** The system, implemented in `main.py`, provides real-time X and Y coordinates, as well as the area of the tracked ball.

## Setup

1. **Install Dependencies:**
   - Make sure you have the necessary dependencies installed by running:

     ```bash
     pip install -r requirements.txt
     ```

2. **Run Setup:**
   - Execute `ball_setup.py` to set the color of the ball:
     ```bash
     python setup.py
     ```
   - Adjust the HSV parameters using the trackbars to match the color of the ball.

3. **Run Ball Tracking:**
   - Use the obtained HSV values in `main.py` for color-based tracking:
     ```bash
     python main.py
     ```

## Code Files

### `main.py`

This file contains the main implementation of the real-time ball tracking system. It captures video from the webcam, tracks the ball based on the specified color, and provides continuous updates on the X and Y coordinates, as well as the area of the tracked ball.

### `setup.py`

Use this file to set the color of the ball interactively. It opens a window with four partitions, displaying the normal video, color image, mask, and an empty partition. Additionally, the trackbars helps adjust the HSV parameters for color detection.

Tutorial for ball setup:

https://github.com/Yaszh/ball_tracking_system/assets/71252244/e2243d66-ed93-47d1-a0d3-ce412f8b21c7


## Dependencies

- `cvzone`: CVZONE library for computer vision tasks.
- `opencv-python`: OpenCV library for image processing.
- `serial`: Python library for serial communication (used for demonstration purposes).

## Usage

1. Run `ball_setup.py` to interactively set the color of the ball.
2. Copy the obtained HSV values.
3. Paste the HSV values into `main.py`.
4. Run `main.py` to initiate real-time ball tracking.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## Acknowledgements

Special thanks to Murtaza's Workshop for providing insightful tutorials and guidance. This project was made possible with the help of their excellent content.

- [Murtaza's Workshop - Robotics and AI](https://www.youtube.com/@murtazasworkshop)


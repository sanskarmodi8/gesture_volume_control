# Gesture Volume Control

## Overview

This project utilizes the MediaPipe and OpenCV libraries in Python to create a real-time gesture-based volume control system. The hand-tracking module detects the user's hand gestures, and based on the position of the hand landmarks, adjusts the system volume accordingly.

![resultGIF](https://github.com/sanskarmodi8/gesture_volume_control/blob/main/result.gif)

## Features

- Hand detection and landmark tracking using MediaPipe.
- Gesture-based volume control by interpreting hand movements.
- Real-time visualization of volume changes on the screen.

## Requirements

- Python 3
- OpenCV
- MediaPipe
- NumPy
- PulseAudio
- Hand Tracking Module

## Installation

1. Install the required Python libraries:

   ```bash
   pip install opencv-python mediapipe numpy pulsectl
   ```

2. Clone the repository:

   ```bash
   git clone https://github.com/your-username/gesture-volume-control.git
   ```

3. Run the `gesture_vol_control.py` script:

   ```bash
   cd gesture-volume-control
   python gesture_vol_control.py
   ```

## Usage

1. Execute the `gesture_vol_control.py` script.

2. Position your hand in front of the camera.

3. Interact with the system volume by adjusting the distance between your thumb and index finger.

4. The program displays the current volume percentage on the screen.

## Acknowledgments

- MediaPipe: [https://google.github.io/mediapipe/](https://google.github.io/mediapipe/)
- OpenCV: [https://opencv.org/](https://opencv.org/)

## Troubleshooting

- If you encounter issues with PulseAudio, ensure that it is properly configured on your system.

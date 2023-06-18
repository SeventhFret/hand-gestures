# Landmarks recognition project with Mediapipe in Python with camera on Freenove ESP32-WROVER-Cam-board

![Motherboard pic](/docs/main-pic.jpg)


## Table of contents

1. [Description](#description)
2. [Technologies](#technologies)
    + [Hardware](#hardware)
    + [Software](#software)
3. [Gestures](#gestures)
    + [First gesture](#first-gesture)
    + [Second gesture](#second-gesture)
    + [Third gesture](#third-gesture)
4. [Credits](#credits)

## Description

This project can recognize few gestures and commit actions according to them.
For now, project has only four main gestures:
+ Volume change mode
+ Cursor move mode
+ Click mode
+ Press Space(for macOS preview function)

---

## Technologies
Technologies that have been used in project

### Hardware
+ Freenove ESP32-WROVER-Cam board
+ Omni Vision 2640 Camera module
### Software
+ Python
+ Mediapipe
+ opencv
+ pyautogui
+ osascript

---

## Gestures

### First gesture 
is change volume. You have to put up your thumb and indexing finger, and according to distance between them, you can change volume. When you choosed your desired volume level - simply keep fingers in that position for 3 seconds, afterwards - volume will be changed.


![First gesture pic](/docs/first-gesutre.jpg)

---

### Second gesture

is to move the cursor. To do so, you have to put up your indexing finger, and then you'll see space, where you can move your finger. If you want to make click - you can put up middle finger along with indexing one, and this will click the mouse.

![Second gesture pic](/docs/second-gesture.jpg)

### Third gesture
is to put up your indexing and middle finger in the same time, that will press Space key of your keyboard. This made to open previews on macOS.


---

## Credits

My project based on two other projects, and my code is NOT UNIQUE. I used code from two developers, and based on that, I've built additional functionality.

Resources:
+ [How to electronics.](https://how2electronics.com/gesture-controlled-virtual-mouse-with-esp32-cam-opencv/)  Author: Priyansh Shankhdhar
+ [CV Zone](https://www.computervision.zone/courses/gesture-volume-control/)

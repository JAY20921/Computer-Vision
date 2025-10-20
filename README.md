# Computer Vision Projects

Welcome to my collection of computer vision projects! This repository contains multiple projects using Python and OpenCV, showcasing real-time color detection, face recognition, human detection, object detection, robotic arm control, ARUCO marker detection, camera calibration, GUI automation, and server communication.

---

## Projects Overview

### 1. Colours Detection

**Description**: Detects and identifies colors of objects in real-time using a webcam feed. Utilizes HSV color space for better segmentation.

**How to Run**:

```bash
python "Colours Detection.py"
```

**Dependencies**: opencv-python, numpy

### 2. Face Recognition

**Description**: Detects and recognizes faces using OpenCV's Haar Cascade and LBPH.

**How to Run**:

```bash
python "Face_recognition.py"
```

**Dependencies**: opencv-python

### 3. Human Detector

**Description**: Detects humans in real-time using pre-trained MobileNet SSD.

**How to Run**:

```bash
python "Human Detector.py"
```

**Dependencies**: opencv-python

### 4. Object Detection

**Description**: Performs object detection using a pre-trained MobileNet SSD model.

**How to Run**:

```bash
python "OBJECT_DETECTION.py"
```

**Dependencies**: opencv-python

### 5. PYAutoGUI Automation

**Description**: Automates GUI interactions such as mouse and keyboard actions.

**How to Run**:

```bash
python "PYAutoGUI.py"
```

**Dependencies**: pyautogui

### 6. ROBOTIC ARM Control

**Description**: Controls a robotic arm using visual feedback and inverse kinematics.

**How to Run**:

```bash
python "ROBOTIC_ARM.py"
```

**Dependencies**: opencv-python, numpy

### 7. ARUCO Marker Detection

**Description**: Detects ARUCO markers in real-time.

**How to Run**:

```bash
python "aruco.py"
```

**Dependencies**: opencv-contrib-python

### 8. Camera Calibration

**Description**: Calibrates camera using chessboard patterns to compute intrinsic and extrinsic parameters.

**How to Run**:

```bash
python "calibration.py"
```

**Dependencies**: opencv-python

### 9. Server Communication

**Description**: Implements server-client communication using sockets for transmitting image data.

**How to Run**:

```bash
python "Server.py"
```

**Dependencies**: socket

---

## Setup Instructions

1. **Clone the repository**:

```bash
git clone https://github.com/JAY20921/Computer-Vision.git
cd Computer-Vision
```

2. **Create a virtual environment**:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Run any project script**:

```bash
python <script_name.py>
```

Replace `<script_name.py>` with the script you want to run.

---


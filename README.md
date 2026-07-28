# AI Fitness Tracker & Form Analyzer

A Python-based Computer Vision pet project for real-time fitness tracking, joint angle calculation, and automatic repetition counting.

## Features
- 🎥 **Real-time Pose Detection:** Leverages **MediaPipe Pose** to detect 33 skeletal landmarks.
- 📐 **Vector Math Calculations:** Computes exact joint angles in 2D space using **NumPy** vector algebra.
- 🧠 **Finite State Machine (FSM):** Handles motion phases (`UP`/`DOWN`) to ensure precise repetition counting without false triggers.
- 📊 **Interactive Dashboard:** Built-in **OpenCV** UI displaying live rep counts, current state, and an interpolated visual progress bar.

## Tech Stack
- **Python 3.12**
- **OpenCV** (Video stream capture & UI rendering)
- **MediaPipe 0.10.14** (Pose landmark detection)
- **NumPy** (Vector operations)

## 📁 Project Structure

```text
ai-fitness-tracker/
├── src/
│   ├── utils.py          # Vector algebra and angle calculation logic
│   └── pose_detector.py # MediaPipe Pose detector wrapper class
├── main.py               # Main pipeline, state machine & OpenCV UI
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
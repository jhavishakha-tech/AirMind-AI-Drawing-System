# 🚀 AirMind AI – Gesture Controlled Drawing System

A real-time computer vision application that enables users to draw and interact with a digital canvas using hand gestures, eliminating the need for traditional input devices.

---

## 🎯 Key Features

* ✍️ Air drawing using index finger
* 🎨 Real-time color selection (Red, Green, Blue, Pink)
* 🧽 Dual erase modes (two-finger and wrist-based)
* ✊ Fist gesture to clear entire canvas
* 🤏 Pinch gesture for dynamic brush size control
* 🎲 Gesture-triggered random color switching
* ⚡ Smooth stroke generation using motion smoothing

---

## 🎥 Demo

👉 https://drive.google.com/file/d/1L_eI6zuYgifRw25UfKqRUTemcbM86A8k/view?usp=drivesdk

---

## 🛠️ Tech Stack

* Python
* OpenCV
* MediaPipe
* NumPy

---

## ⚙️ Setup & Execution

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
py -3.10 hand_tracking.py
```

---

## 🎮 Gesture Mapping

| Gesture             | Function          |
| ------------------- | ----------------- |
| Index Finger        | Draw              |
| Two Fingers         | Erase             |
| Wrist Movement      | Large Erase       |
| Fist                | Clear Screen      |
| Pinch               | Adjust Brush Size |
| Top Bar Interaction | Change Color      |
| Special Gesture     | Random Color      |

---

## 💡 Implementation Overview

The system uses MediaPipe to detect hand landmarks in real time.
Finger positions are analyzed to interpret gestures, which are then mapped to drawing actions using OpenCV.
A smoothing mechanism is applied to ensure stable and visually clean strokes.

---

## 🚀 Future Enhancements

* Deep learning-based gesture recognition for improved accuracy
* Context-aware interaction system for intelligent mode switching

---

## 👩‍💻 Author

**Vishakha Jha**
Computer Science Engineering Student

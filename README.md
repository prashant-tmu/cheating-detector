# Eye Gaze Tracker 👁️👀

A real-time eye gaze detection project using **Python**, **OpenCV**, and **MediaPipe**.  
This script detects facial landmarks and tracks the left eye's iris position to determine whether the user is looking **left**, **right**, or **center**.

---

## 🔍 Features

- Real-time webcam-based eye tracking
- Face and iris landmark detection using MediaPipe FaceMesh
- Determines if the user is:
  - 👈 Looking Left
  - 👉 Looking Right
  - 👁️ Looking Center
- Displays gaze direction on screen

---

## 🛠️ Technologies Used

- [Python](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [MediaPipe](https://developers.google.com/mediapipe)

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/eye-gaze-tracker.git
cd eye-gaze-tracker
2. Install Dependencies
bash
Copy
Edit
pip install opencv-python mediapipe
3. Run the Script
bash
Copy
Edit
python gaze_tracker.py
⚠️ Make sure your webcam is enabled and accessible.
Press Esc to quit the app.

🧠 How It Works
Uses MediaPipe's FaceMesh model to detect 468 facial landmarks.

Identifies:

Left eye outer corner (Landmark 33)

Left eye inner corner (Landmark 133)

Left iris center (Landmark 468)

Calculates the iris's position relative to the eye corners to determine gaze direction.

📂 File Structure
bash
Copy
Edit
eye-gaze-tracker/
├── gaze_tracker.py   # Main script file
├── README.md         # Project documentation
✅ To-Do / Future Improvements
 Add right eye tracking

 Add blink detection

 Track multiple faces

 Head pose estimation

 Convert to desktop or web application

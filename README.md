Eye Gaze Tracker 👁️👀
A real-time eye gaze detection project using Python, OpenCV, and MediaPipe. This script detects facial landmarks and tracks the left eye's iris position to determine whether the user is looking left, right, or center.

🔍 Features
Real-time face and eye landmark detection

Iris tracking using MediaPipe's Face Mesh

Calculates gaze direction: Left, Right, or Center

Simple and interactive UI with OpenCV

📷 Demo
Add a screen recording or image here (optional but highly recommended)

🛠️ Technologies Used
Python

OpenCV

MediaPipe

🚀 Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/eye-gaze-tracker.git
cd eye-gaze-tracker
Install dependencies:

bash
Copy
Edit
pip install opencv-python mediapipe
Run the script:

bash
Copy
Edit
python gaze_tracker.py
Press Esc to quit the app.

📂 File Structure
bash
Copy
Edit
eye-gaze-tracker/
├── gaze_tracker.py   # Main Python script
├── README.md         # Project documentation
🤓 How It Works
MediaPipe Face Mesh provides 468 3D facial landmarks.

The script uses landmarks 33 and 133 for the outer and inner left eye corners.

Landmark 468 is used to locate the center of the left iris.

The script calculates the horizontal iris position relative to the eye to determine gaze direction.

🧠 Future Improvements
Add right eye tracking

Blink detection

Head pose estimation

Web version using JavaScript and TensorFlow.js

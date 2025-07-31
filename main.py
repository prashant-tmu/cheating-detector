import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = face_mesh.process(rgb_frame)

    if result.multi_face_landmarks:
        for face_landmarks in result.multi_face_landmarks:
            h, w, _ = frame.shape

            left_eye_outer = face_landmarks.landmark[33]
            left_eye_inner = face_landmarks.landmark[133]

            left_iris = face_landmarks.landmark[468]

            outer_x = int(left_eye_outer.x * w)
            inner_x = int(left_eye_inner.x * w)
            iris_x = int(left_iris.x * w)
            iris_y = int(left_iris.y * h)

            cv2.circle(frame, (iris_x, iris_y), 4, (0, 255, 255), -1)
            cv2.circle(frame, (outer_x, int(left_eye_outer.y * h)), 2, (0, 255, 0), -1)
            cv2.circle(frame, (inner_x, int(left_eye_inner.y * h)), 2, (0, 255, 0), -1)

            eye_range = inner_x - outer_x
            iris_offset = iris_x - outer_x
            iris_ratio = iris_offset / eye_range if eye_range != 0 else 0.5

            if iris_ratio < 0.40:
                gaze = "Looking Left 👀"
            elif iris_ratio > 0.60:
                gaze = "Looking Right 👀"
            else:
                gaze = "Looking Center ✅"

            cv2.putText(frame, gaze, (30, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)

    else:
        cv2.putText(frame, "No Face Detected ❌", (30, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Eye Gaze Tracker', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
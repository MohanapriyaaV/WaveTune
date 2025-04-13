import cv2
import numpy as np
from media_player import MediaPlayer
from gesture_control import gesture_to_action

# Dummy prediction function (replace with real model later)
def predict_gesture(frame):
    # For demo: count white pixels and use thresholds
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    white_pixels = cv2.countNonZero(thresh)

    if white_pixels > 50000:
        return "play"
    elif 20000 < white_pixels <= 50000:
        return "pause"
    else:
        return "none"

# Init Media Player
media_path = "D:\\SEM - 6\\Vista Engg Hackathon\\gesture_media_player\\WaveTune\\song.mp3"  # Keep it in the same folder for now
player = MediaPlayer(media_path)

# Init webcam
cap = cv2.VideoCapture(0)

print("[INFO] Press 'q' to exit the app")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gesture = predict_gesture(frame)

    if gesture != "none":
        gesture_to_action(gesture, player)

    cv2.putText(frame, f"Gesture: {gesture}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
player.stop()

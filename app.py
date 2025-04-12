import cv2
import numpy as np
import pyautogui
import pygame
import threading

# Initialize pygame for media controls
pygame.mixer.init()
pygame.mixer.music.load("D:\\SEM - 6\\Vista Engg Hackathon\\gesture_media_player\\WaveTune\\song.mp3")  # Replace with your media file path
pygame.mixer.music.play()

# Gesture control function
def gesture_control(gesture):
    if gesture == "raise_hand":
        pyautogui.press('playpause')  # Play/Pause media
    elif gesture == "left_swipe":
        pyautogui.press('nexttrack')  # Next track
    elif gesture == "right_swipe":
        pyautogui.press('prevtrack')  # Previous track

# Initialize the webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Function for handling webcam feed and gesture detection
def capture_webcam():
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (15, 15), 0)
        edges = cv2.Canny(blurred, 50, 150)
        contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > 500:
                hull = cv2.convexHull(contour)
                cv2.drawContours(frame, [hull], -1, (0, 255, 0), 3)

                # Detect gesture based on contour characteristics (placeholder logic)
                gesture_control("raise_hand")

        cv2.imshow("Gesture Control Media Player", frame)

        # Break if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Start the webcam feed in a separate thread
thread = threading.Thread(target=capture_webcam)
thread.start()

# Wait for the thread to finish
thread.join()

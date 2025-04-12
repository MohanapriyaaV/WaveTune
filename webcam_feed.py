import cv2
import numpy as np

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Set frame width and height
cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and improve the detection
    blurred = cv2.GaussianBlur(gray, (15, 15), 0)

    # Use the Canny edge detector to detect edges
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the frame
    for contour in contours:
        if cv2.contourArea(contour) > 500:
            # Find the convex hull of the contour
            hull = cv2.convexHull(contour)
            cv2.drawContours(frame, [hull], -1, (0, 255, 0), 3)

    # Display the frame with detected contours
    cv2.imshow("Gesture Control Media Player", frame)

    # Quit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

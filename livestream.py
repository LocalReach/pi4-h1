import cv2
import subprocess

# Initialize the video capture from the first camera device
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open video capture device.")
    exit()

# Set the window to be named 'video' and make it fullscreen
cv2.namedWindow('video', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Can't receive frame (stream end?). Exiting ...")
        break

    # Display the resulting frame in fullscreen mode
    cv2.imshow('video', frame)

    # Wait for the 'w' key to be pressed to exit
    if cv2.waitKey(1) & 0xFF == ord('w'):
        break

# When everything done, release the capture and destroy all windows
cap.release()
cv2.destroyAllWindows()


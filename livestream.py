import cv2
import time

# Initialize the video capture from the first camera device
cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cap.set(cv2.CAP_PROP_FPS, 60)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open video capture device.")
    exit()

# Set the window to be named 'video' and make it fullscreen
cv2.namedWindow('video', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Initialize variables for calculating FPS
frame_count = 0
fps = 0
start_time = time.time()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Can't receive frame (stream end?). Exiting ...")
        break

    # Increment frame count
    frame_count += 1

    # Calculate FPS every second
    current_time = time.time()
    if (current_time - start_time) > 1:
        fps = frame_count / (current_time - start_time)
        frame_count = 0
        start_time = time.time()

    # Put FPS on the frame
    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Display the resulting frame in fullscreen mode
    cv2.imshow('video', frame)

    # Wait for the 'w' key to be pressed to exit
    if cv2.waitKey(1) & 0xFF == ord('w'):
        break

# When everything done, release the capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
from ultralytics import YOLO
import cv2
import time

# Create a named window for displaying the output
cv2.namedWindow('YOLOv8', cv2.WINDOW_NORMAL)

# URL for the real-time video stream
video_url = 'https://trafficvideo2.tainan.gov.tw/b596d902'

model = YOLO('yolov8m.pt')  # Load YOLOv8 model

# Open video capture from the real-time stream
cap = cv2.VideoCapture(video_url)
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

while True:
    st = cv2.getTickCount()  # Start timing
    r, frame = cap.read()
    if not r:
        print("Error: Could not read frame.")
        break

    # Apply YOLO model
    results = model(frame, verbose=False)
    frame = results[0].plot()

    et = cv2.getTickCount()  # End timing
    fps = cv2.getTickFrequency() / (et - st)  # Calculate FPS

    # Display FPS on the frame
    cv2.putText(frame, 'FPS=' + str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 255), 2)
    cv2.imshow('YOLOv8', frame)

    # Exit on 'Esc' key press
    key = cv2.waitKey(1)
    if key == 27:
        break

# Cleanup resources
cap.release()
cv2.destroyAllWindows()

import cv2
import matplotlib.pyplot as plt

# To access the camera
cap= cv2.VideoCapture(0)

# To read/capture image
ret, frame = cap.read()
plt.imshow(frame)
plt.title("This is first image capture from camera")
plt.show()

# To off the camera
cap.release()

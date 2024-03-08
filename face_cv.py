# To detect face from from image
import cv2

# To import dataset-cascade(haarcascade dataset)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("group1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("This is a group image",gray)

# Find the coordinates of the gray image
face = face_cascade.detectMultiScale(gray,1.05,6)
for x,y,w,h in face:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)


cv2.imshow("face detect in image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
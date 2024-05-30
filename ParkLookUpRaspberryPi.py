import cv2
import pickle

img = cv2.imread('ParLookUp_Park.jpg')

while True:

    cv2.rectangle(img, (100, 100), (200, 150), (255, 0, 255), 2)
    cv2.imshow("Park Image", img)
    cv2.waitKey(1)
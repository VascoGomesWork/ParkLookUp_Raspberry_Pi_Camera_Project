import cv2
import pickle

img = cv2.imread('ParkLookUpPark.jpg')

width, height = 450, 335
pos_list = []

def mouse_click(events, x, y, flags, params):
    
    if events == cv2.EVENT_LBUTTONDOWN:
        pos_list.append(((x + 180), (y + 250)))


while True:
    #                    X    Y      X  - Y         Cor    Espessura
    #cv2.rectangle(img, (300, 385), (750, 720), (255, 0, 255), 3)
    
    for pos in pos_list:
        cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height), (255, 0, 255), 3)
    
    img_resized = cv2.resize(img, (600, 700))
    cv2.imshow("ParkImage", img_resized)
    
    cv2.setMouseCallback("ParkImage", mouse_click)
    
    cv2.waitKey(1)

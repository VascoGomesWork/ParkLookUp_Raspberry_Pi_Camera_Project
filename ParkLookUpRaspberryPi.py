import cv2
import pickle

width, height = 125, 98

try:
    with open("ParkLookUpParkPositions", "rb") as f:
        #Gets the Image Marks from the previous Run and Shows
        pos_list = pickle.load(f)
except:
    pos_list = []

def mouse_click(events, x, y, flags, params):
    
    if events == cv2.EVENT_LBUTTONDOWN:
        pos_list.append((x, y))
        
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(pos_list):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                pos_list.pop(i)
                
    with open("ParkLookUpParkPositions", "wb") as f:
        pickle.dump(pos_list, f)


while True:
    #In order to delete the rectangles the image needs to be constantly generated
    img = cv2.imread('ParkLookUpPark2.jpg')
    
    #                    X    Y      X  - Y         Cor    Espessura
    #cv2.rectangle(img, (45, 37), (170, 135), (255, 0, 255), 3)
    
    for pos in pos_list:
        cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height), (255, 0, 255), 3)
    
    cv2.imshow("ParkImage", img)
    
    cv2.setMouseCallback("ParkImage", mouse_click)
    
    cv2.waitKey(1)

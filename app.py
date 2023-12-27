import cvzone
import numpy as np
import cv2
import pickle

with open("carpositions", "rb") as f:
    positions = pickle.load(f)

width = 35
height = 15

cap = cv2.VideoCapture("./output_video.mp4")


def check(imgproc):
    spaces = 0
    for position in positions:
        x, y = position

        imgcrp = imgproc[y : y + height, x : x + width]

        # cv2.imshow(str(x+y),imgcrp)
        count = cv2.countNonZero(imgcrp)
        

        if count < 30:
            color = (0, 255, 0)
            thickness = 1
            spaces += 1
        else:
            color = (0, 0, 255)
            thickness = 1


        # mostatil har space
        cv2.rectangle(
            img, position, (position[0] + width, position[1] + height), color, thickness
        )
        
        
        # pixel dakhele har space
        cvzone.putTextRect(
            img,
            str(count),
            (x, y + height - 2),
            scale=0.7,
            thickness=1,
            offset=0,
            colorR=color,
        )
        
        
        
        # shomaresh
        cvzone.putTextRect(
            img,
            f" Free : {spaces} / {len(positions)}",
            (20, 30),
            scale=2,
            thickness=1,
            offset=2,
            colorR=(25,25,25),
        )


while True:
    s, img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgthreshold = cv2.adaptiveThreshold(
        imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16
    )
    imgmed = cv2.medianBlur(imgthreshold, 3)
    kern = np.ones((1, 1), np.uint8)
    imgDi = cv2.dilate(imgmed, kern, iterations=1)

    check(imgDi)

    cv2.imshow("img", img)
    # cv2.imshow("imgDi", imgDi)
    cv2.waitKey(10)

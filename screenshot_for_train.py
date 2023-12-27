import cv2
import os
import time

cam = cv2.VideoCapture("./output_video.mp4")

try:
    if not os.path.exists("data"):
        os.makedirs("data")

except OSError:
    print("Error: Creating directory of data")

intvl = 2  # interval in second(s)

fps = int(cam.get(cv2.CAP_PROP_FPS))
print("fps : ", fps)

currentframe = 0

ret, frame = cam.read()
if ret:
    if currentframe % (fps * intvl) == 0:
        name = "./data/frame" + str(currentframe) + ".jpg"
        print("Creating..." + name)
        cv2.imwrite(name, frame)

cam.release()
cv2.destroyAllWindows()

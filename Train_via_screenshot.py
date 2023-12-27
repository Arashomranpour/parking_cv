import cv2
import pickle


try:
    with open("carpositions", "rb") as f:
        positions = pickle.load(f)

except:
    positions = []

width = 35
height = 15


def mouseclick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        positions.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(positions):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                positions.pop(i)
    with open("carpositions", "wb") as f:
        pickle.dump(positions, f)


while True:
    img = cv2.imread("./data/frame0.jpg")
    img = cv2.resize(img, (1280, 720))

    for position in positions:
        cv2.rectangle(
            img, position, (position[0] + width, position[1] + height), (255, 0, 255), 2
        )

    cv2.imshow("img", img)
    cv2.setMouseCallback("img", mouseclick)
    cv2.waitKey(1)
    # if cv2.waitKey(0) & 0xFF == ord("q"):
    #     break

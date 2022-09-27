import cv2
from pytesseract import image_to_string

def image_to_text(frame):
    return image_to_string(frame)

can = cv2.VideoCapture('Output.mp4')
value = 0
flag = ''
while 1:
    frame = can.read()[1]
    cv2.imwrite["frame"+str(value)+".png",frame]
    flag += image_to_text(frame)
    cv2.waitKey[1]
    value += 1
    if value == 4:
        break
print(flag)
can.release()
cv2.destroyAllWindows()
import cvzone
from cvzone.ColorModule import ColorFinder
import cv2

capture= cv2.VideoCapture(0)
capture.set(3,1080)
capture.set(4,720)

success,img = capture.read()
h,w,c=img.shape

finder= ColorFinder(True)
hsvVals={'hmin': 17, 'smin': 125, 'vmin': 32, 'hmax': 41, 'smax': 255, 'vmax': 249}

while True:
    success,img = capture.read()
    color_img, mask= finder.update(img,hsvVals)

    imgStack= cvzone.stackImages([img,color_img,mask],2,0.5)
    cv2.imshow("setup", imgStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

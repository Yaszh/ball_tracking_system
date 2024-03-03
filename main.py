import cvzone
from cvzone.ColorModule import ColorFinder
import cv2
import serial  # Import the serial library



capture = cv2.VideoCapture(0)
capture.set(3, 1080)
capture.set(4, 720)

success, img = capture.read()
h, w, c = img.shape

finder = ColorFinder(False)
hsvVals = {'hmin': 19, 'smin': 77, 'vmin': 11, 'hmax': 36, 'smax': 255, 'vmax': 255}

while True:
    success, img = capture.read()
    color_img, mask = finder.update(img, hsvVals)
    img_contour, contours = cvzone.findContours(img, mask)

    if contours:
        x, y, z = contours[0]['center'][0], h - contours[0]['center'][1], int(contours[0]['area'])
        print(f"X: {x}, Y: {y}, Z: {z}")

        # # Send the coordinates as a string over the COM port
        # coordinates_str = f"X: {x}, Y: {y}, Z: {z}\n"
        # ser.write(coordinates_str.encode())  # Send the string as bytes

    cv2.imshow("Tracking", img_contour)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the COM port when done
# ser.close()

capture.release()
cv2.destroyAllWindows()

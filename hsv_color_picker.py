import cv2
import numpy as np

# Dummy callback for trackbar (required by createTrackbar)
def nothing(x):
    pass

# Create a window named "frame"
cv2.namedWindow("frame")

# Create trackbars for H, S, V values
cv2.createTrackbar("H", "frame", 0, 179, nothing)
cv2.createTrackbar("S", "frame", 0, 255, nothing)
cv2.createTrackbar("V", "frame", 0, 255, nothing)

# Create an HSV image (blank initially)
img_hsv = np.zeros((250, 500, 3), np.uint8)

while True:
    # Get current positions of the trackbars
    h = cv2.getTrackbarPos("H", "frame")
    s = cv2.getTrackbarPos("S", "frame")
    v = cv2.getTrackbarPos("V", "frame")

    # Fill the HSV image with the selected color
    img_hsv[:] = (h, s, v)

    # Convert HSV to BGR for display
    img_bgr = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

    # Show the image
    cv2.imshow("frame", img_bgr)

    # Break loop on ESC key (key code 27)
    key = cv2.waitKey(1)
    if key == 27:
        break

# Clean up windows after exit
cv2.destroyAllWindows()

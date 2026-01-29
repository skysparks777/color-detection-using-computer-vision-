import cv2
import numpy as np

def detect_color(hue, sat, val):
    if val < 50:
        return "BLACK"
    elif sat < 50:
        if val > 200:
            return "WHITE"
        else:
            return "GRAY"
    else:
        if hue < 5 or hue >= 170:
            return "RED"
        elif hue < 10:
            return "DARK RED"
        elif hue < 22:
            return "ORANGE"
        elif hue < 30:
            return "GOLDEN YELLOW"
        elif hue < 35:
            return "YELLOW"
        elif hue < 45:
            return "LIGHT GREEN"
        elif hue < 78:
            return "GREEN"
        elif hue < 90:
            return "AQUA"
        elif hue < 100:
            return "CYAN"
        elif hue < 110:
            return "SKY BLUE"
        elif hue < 131:
            return "BLUE"
        elif hue < 145:
            return "INDIGO"
        elif hue < 160:

            
            return "VIOLET"
        elif hue < 170:
            return "MAGENTA"
    return "UNDEFINED"

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Get frame center pixel
        height, width, _ = frame.shape
        center_x = width // 2
        center_y = height // 2

        # Convert to HSV and get center pixel
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        pixel_hsv = hsv_frame[center_y, center_x]
        hue, sat, val = pixel_hsv

        # Get BGR for text color contrast
        pixel_bgr = frame[center_y, center_x]

        # Detect color name
        color_name = detect_color(hue, sat, val)

        # Draw circle and text
        cv2.circle(frame, (center_x, center_y), 10, (0, 255, 0), 2)
        cv2.putText(frame, f"{color_name}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (int(pixel_bgr[0]), int(pixel_bgr[1]), int(pixel_bgr[2])), 2)

        cv2.imshow("Color Detection", frame)

        # Exit on ESC key
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

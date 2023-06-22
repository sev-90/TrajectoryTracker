import numpy as np
import cv2
from IPython.display import Video
from matplotlib import pyplot as plt

np.random.seed(42)
CAMERA_NAME = 'Mudd2'
img = cv2.imread('cameraViewImg_{}.jpg'.format(CAMERA_NAME))

#Routine to fix 
def fixColor(image):
    return(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))


# Define the callback function for mouse events
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Left button clicked at pixel (x={}, y={})".format(x, y))
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("Right button clicked at pixel (x={}, y={})".format(x, y))

# Read an image or create a blank one
image = fixColor(img)

# Create a named window to display the image
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

# Set the mouse callback function for the window
cv2.setMouseCallback("Image", mouse_callback)

while True:
    # Display the image in the window
    cv2.imshow("Image", image)

    # Wait for a key press and check if 'q' is pressed to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up and close the windows
cv2.destroyAllWindows()
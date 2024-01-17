import numpy as np
import cv2

# Load the image using cv2.imread()
img = cv2.imread('photo/images.jpg')

# Check if the image was loaded successfully
if img is not None:
    # Display the original image using cv2.imshow()
    cv2.imshow('Original Image', img)

    # Get the dimensions of the image
    h, w, channels = img.shape
    print("Height:", h)
    print("Width:", w)
    print("Channels:", channels)

    # Create an empty array to store the negative image
    neg_img = np.zeros_like(img)

    # Compute the negative image
    for x in range(h):
        for y in range(w):
            neg_img[x, y] = 255 - img[x, y]

    print("Negative image calculated")

    # Display the negative image using cv2.imshow()
    cv2.imshow('Negative Image', neg_img)

    # Wait for a key press and close the window on key press
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error loading image")

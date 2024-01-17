import cv2
import numpy as np

def apply_high_pass_filter(image, cutoff_frequency):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply DFT to the image
    dft = cv2.dft(np.float32(gray_image), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)

    # Create a mask for the high-pass filter
    rows, cols = gray_image.shape
    center_row, center_col = rows // 2, cols // 2
    mask = np.zeros((rows, cols), np.uint8)
    mask[center_row - cutoff_frequency:center_row + cutoff_frequency,
         center_col - cutoff_frequency:center_col + cutoff_frequency] = 1

    # Apply the mask to the frequency domain representation
    dft_shift = dft_shift * mask

    # Inverse DFT to get back to the spatial domain
    inverse_dft = np.fft.ifftshift(dft_shift)
    img_back = cv2.idft(inverse_dft)
    img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

    return np.uint8(img_back)

# Example usage
image = cv2.imread('goldengate.jpg.jpg')
cutoff_frequency = 30  # Adjust this value based on your requirements
result_high_pass = apply_high_pass_filter(image, cutoff_frequency)

cv2.imshow('Original Image', image)
cv2.imshow('High Pass Filtered Image', result_high_pass)
cv2.waitKey(0)
cv2.destroyAllWindows()

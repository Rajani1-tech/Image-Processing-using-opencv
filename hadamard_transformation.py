import cv2
import numpy as np

def hadamard_transform(img):
    # Check if the image dimensions are powers of 2
    rows, cols = img.shape
    if not (cv2.getOptimalDFTSize(rows) == rows and cv2.getOptimalDFTSize(cols) == cols):
        raise ValueError("Image dimensions must be powers of 2 for Hadamard transform.")

    # Perform Hadamard transform
    img_float32 = np.float32(img)
    hadamard_transformed = cv2.dct(cv2.dct(img_float32).T).T

    return hadamard_transformed

def inverse_hadamard_transform(hadamard_transformed):
    # Perform inverse Hadamard transform
    inverted_transformed = cv2.idct(cv2.idct(hadamard_transformed).T).T

    # Clip values to the valid range [0, 255]
    inverted_transformed = np.clip(inverted_transformed, 0, 255)

    return np.uint8(inverted_transformed)

# Example usage
image = cv2.imread('photo/downtown.jpeg', cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (512, 512))  # Resize to a power of 2 for simplicity

# Perform Hadamard transform
hadamard_result = hadamard_transform(image)

# Perform inverse Hadamard transform
inverse_hadamard_result = inverse_hadamard_transform(hadamard_result)

# Display the original and reconstructed images
cv2.imshow('Original Image', image)
cv2.imshow('Hadamard Transformed Image', hadamard_result)
cv2.imshow('Reconstructed Image', inverse_hadamard_result)
cv2.waitKey(0)
cv2.destroyAllWindows()

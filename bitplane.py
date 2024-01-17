import cv2
import numpy as np

img = cv2.imread('photo/dollar.jpg', 0)
lst = []

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        lst.append(np.binary_repr(img[i][j], width=8))

bit_planes = []
for bit in range(8):
    bit_plane = (np.array([int(i[bit]) for i in lst], dtype='uint8') * (2 ** (7 - bit))).reshape(img.shape[0], img.shape[1])
    bit_planes.append(bit_plane)

for bit, plane in enumerate(bit_planes):
    cv2.imwrite(f'bit_plane_{bit}.jpg', plane)

cv2.destroyAllWindows()

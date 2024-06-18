import numpy as np
import pywt
import cv2


def w2d(img, mode='haar', level=1):
    # Convert to grayscale
    imArray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Convert to float and normalize
    imArray = np.float32(imArray) / 255.0

    # Compute wavelet coefficients
    coeffs = pywt.wavedec2(imArray, mode, level=level)

    # Process coefficients: set the approximation coefficients to zero
    coeffs_H = list(coeffs)
    coeffs_H[0] = np.zeros_like(coeffs_H[0])

    # Reconstruct the image from the modified coefficients
    imArray_H = pywt.waverec2(coeffs_H, mode)
    imArray_H = np.uint8(imArray_H * 255)  # Convert back to uint8

    return imArray_H
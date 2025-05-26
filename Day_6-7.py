import cv2
import os
import numpy as np

# Create output directory if it doesn't exist
os.makedirs("output", exist_ok=True)

# Load the original image (in color)
original = cv2.imread("Grayscale.jpg")

if original is None:
    print("Error: Image not loaded. Check the filename or path.")
else:
    # Save the original color image
    cv2.imwrite("output/original.jpg", original)

    # Convert to grayscale
    grayscale = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("output/grayscale.jpg", grayscale)

    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(grayscale, (7, 7), 0)
    cv2.imwrite("output/blurred_grayscale.jpg", blurred)

    # Apply more detailed Canny Edge Detection (lower thresholds)
    edges = cv2.Canny(blurred, 10, 70)
    cv2.imwrite("output/canny_edges.jpg", edges)

    # Apply Binary Thresholding
    _, thresholded = cv2.threshold(grayscale, 109, 224, cv2.THRESH_BINARY)
    cv2.imwrite("output/binary_threshold.jpg", thresholded)

    # --- Create 2x2 Grid Image ---
    grayscale_bgr = cv2.cvtColor(grayscale, cv2.COLOR_GRAY2BGR)
    blurred_bgr = cv2.cvtColor(blurred, cv2.COLOR_GRAY2BGR)
    edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    thresholded_bgr = cv2.cvtColor(thresholded, cv2.COLOR_GRAY2BGR)

    top_row = np.hstack((grayscale_bgr, blurred_bgr))
    bottom_row = np.hstack((edges_bgr, thresholded_bgr))
    grid_image = np.vstack((top_row, bottom_row))

    # Resize both windows to 800x800
    grid_resized = cv2.resize(grid_image, (1200, 650))
    original_resized = cv2.resize(original, (1200, 650))

    # --- Display ---
    cv2.imshow("Original Image", original_resized)
    cv2.imshow("Processed Results (2x2 Grid)", grid_resized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

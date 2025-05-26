import cv2
import os

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

    # Apply Canny Edge Detection
    edges = cv2.Canny(blurred, 50, 150)
    cv2.imwrite("output/canny_edges.jpg", edges)

    # Apply Binary Thresholding
    _, thresholded = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite("output/binary_threshold.jpg", thresholded)

    # Display results (optional)
    cv2.imshow("Original Image", original)
    cv2.imshow("Grayscale", grayscale)
    cv2.imshow("Blurred Grayscale", blurred)
    cv2.imshow("Canny Edges", edges)
    cv2.imshow("Binary Threshold", thresholded)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

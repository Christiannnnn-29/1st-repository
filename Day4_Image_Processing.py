import cv2

# Load the image (make sure 'your_image.jpg' is in the same folder)
image = cv2.imread("Grayscale.jpg")

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display original and grayscale images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()

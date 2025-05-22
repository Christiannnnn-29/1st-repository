import cv2

# Load the image
image = cv2.imread('Grayscale.jpg')

if image is None:
    print("Error: Image not loaded. Check the filename or path.")
else:
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Resize the image (width=1000, height=800)
    resized_image = cv2.resize(gray_image, (1000, 800))

    # Convert back to BGR to allow colored shapes and text
    gray_bgr = cv2.cvtColor(resized_image, cv2.COLOR_GRAY2BGR)

    # Draw a rectangle (top-left to bottom-right)
    cv2.rectangle(gray_bgr, (50, 50), (200, 200), (0, 255, 0), 2)

    # Add two circles encircling the eyes (approximate positions)
    # Left eye circle
    cv2.circle(gray_bgr, (400, 300), 50, (0, 255, 255), 3)  # yellow circle

    # Right eye circle
    cv2.circle(gray_bgr, (600, 300), 50, (0, 255, 255), 3)  # yellow circle

    # Add text
    cv2.putText(gray_bgr, 'Day 5', (30, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 6)

    # Save the final image
    cv2.imwrite('output/grayscale_with_shapes.jpg', gray_bgr)

    # Display the result
    cv2.imshow('Edited Image', gray_bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

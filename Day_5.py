import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

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
    cv2.circle(gray_bgr, (400, 300), 50, (0, 255, 255), 3)  # left eye
    cv2.circle(gray_bgr, (600, 300), 50, (0, 255, 255), 3)  # right eye

    # Convert to PIL Image for advanced text
    image_pil = Image.fromarray(cv2.cvtColor(gray_bgr, cv2.COLOR_BGR2RGB))

    draw = ImageDraw.Draw(image_pil)
    # Load Castelar font (put Castelar.ttf in your project folder or specify full path)
    font = ImageFont.truetype("Castelar.ttf", 50)  # font size 50 (enlarged)

    # Add text using Pillow
    draw.text((30, 30), "Day 5", font=font, fill=(255, 0, 0))  # Red text

    # Convert back to OpenCV format
    final_image = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)

    # Save the final image
    cv2.imwrite('output/grayscale_with_shapes_and_text.jpg', final_image)

    # Display the result
    cv2.imshow('Edited Image', final_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

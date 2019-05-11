https://realpython.com/traditional-face-detection-python/

photos visages sur : https://www.pexels.com/photo/standing-family-near-fireplace-1648387/

python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
https://www.anaconda.com/distribution/
https://scikit-learn.org/stable/install.html


import cv2 as cv
# Read image from your local file system
original_image = cv.imread('path/to/your-image.jpg')
# Convert color image to grayscale for Viola-Jones
grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)

# Load the classifier and create a cascade object for face detection
face_cascade = cv.CascadeClassifier('path/to/haarcascade_frontalface_alt.xml')

detected_faces = face_cascade.detectMultiScale(grayscale_image)

for (column, row, width, height) in detected_faces:
    cv.rectangle(
        original_image,
        (column, row),
        (column + width, row + height),
        (0, 255, 0),
        2
    )

cv.imshow('Image', original_image)
cv.waitKey(0)
cv.destroyAllWindows()

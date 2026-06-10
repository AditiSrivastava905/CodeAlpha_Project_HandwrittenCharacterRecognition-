import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load trained model
model = load_model("model.h5")

# Get image path
img_path = input("Enter image path: ")

# Read image in grayscale
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# Check if image loaded
if img is None:
    print("Image not found!")
    exit()

# Resize to MNIST size
img = cv2.resize(img, (28, 28))

# Invert colors
img = cv2.bitwise_not(img)

# Normalize
img = img.astype("float32") / 255.0

# Reshape for model
img = img.reshape(1, 28, 28, 1)

# Predict
prediction = model.predict(img)

predicted_digit = np.argmax(prediction)
confidence = np.max(prediction) * 100

print("\nPredicted Digit:", predicted_digit)
print("Confidence: {:.2f}%".format(confidence))
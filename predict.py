import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("model.h5")

img_path = input("Enter image path: ")

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Image not found!")
    exit()

# Resize to 28x28
img = cv2.resize(img, (28, 28))

# Normalize exactly like training
img = img.astype("float32") / 255.0

# Reshape
img = img.reshape(1, 28, 28, 1)

prediction = model.predict(img)

print("Predicted Digit:", np.argmax(prediction))
print("Confidence:", np.max(prediction) * 100, "%")
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = mnist.load_data()

plt.imshow(x_test[0], cmap='gray')
plt.axis('off')
plt.savefig('digit.png')
print("Image saved as digit.png")
print("Actual digit:", y_test[0])
plt.show()
# Handwritten Character Recognition Using Convolutional Neural Networks (CNN)

## 📌 Project Overview

This project implements a Handwritten Character Recognition system using Deep Learning and Convolutional Neural Networks (CNN). The model is trained on the MNIST dataset to accurately recognize handwritten digits (0–9) from input images.

The project demonstrates the application of image processing and deep learning techniques for automated handwritten digit classification.

---

## 🎯 Objective

To develop a machine learning model capable of recognizing handwritten digits from images with high accuracy using a CNN architecture.

---

## 📂 Dataset

### MNIST Handwritten Digits Dataset

- 60,000 Training Images
- 10,000 Testing Images
- Grayscale Images
- Image Size: 28 × 28 Pixels
- Classes: Digits 0–9

The MNIST dataset is one of the most widely used benchmark datasets for image classification and handwritten digit recognition.

---

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- OpenCV
- NumPy
- Matplotlib

---

## 🧠 Model Architecture

The Convolutional Neural Network consists of:

1. Convolution Layer (32 Filters)
2. Max Pooling Layer
3. Convolution Layer (64 Filters)
4. Max Pooling Layer
5. Flatten Layer
6. Dense Layer
7. Output Layer (10 Classes)

---

## ✨ Features

- Handwritten digit recognition
- CNN-based deep learning model
- Image preprocessing and normalization
- Prediction of custom handwritten digit images
- Model saving and loading functionality
- Accuracy visualization during training

---

## 📁 Project Structure

```text
Handwritten_Character_Recognition
│
├── train_model.py
├── predict.py
├── save_test_image.py
├── model.h5
├── digit.png
├── README.md
└── .gitignore
```

---

## 🚀 How to Run the Project

### Step 1: Install Dependencies

```bash
pip install tensorflow opencv-python numpy matplotlib
```

### Step 2: Train the Model

```bash
python train_model.py
```

This will train the CNN model and generate:

```text
model.h5
```

### Step 3: Predict a Digit

```bash
python predict.py
```

Enter the image path when prompted.

Example:

```text
digit.png
```

---

## 📊 Results

The trained CNN model achieves high accuracy on the MNIST dataset and successfully predicts handwritten digits from image inputs.

---

## 🔮 Future Enhancements

- Extend the project to EMNIST for alphabet recognition
- Support handwritten character recognition (A–Z)
- Implement word and sentence recognition using CRNN
- Develop a graphical user interface (GUI)
- Deploy as a web application

---

## 📚 Learning Outcomes

Through this project, the following concepts were explored:

- Deep Learning Fundamentals
- Convolutional Neural Networks (CNN)
- Image Classification
- Data Preprocessing
- Model Training and Evaluation
- Computer Vision Applications

---

## 👩‍💻 Author

**Aditi Srivastava**

B.Tech CSE (AI & ML)

---



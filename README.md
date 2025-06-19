# Sudoku_Solver
A project that can solve any sudoku live .
🧩 Real-Time Sudoku Solver (Live + Image-based)
A computer vision and deep learning project to detect and solve Sudoku puzzles — works on live webcam feeds and static image files!
Digit recognition powered by a CNN model trained on the MNIST dataset.
Solving algorithm based on backtracking.

🚀 Features
📸 Input options:

Live webcam feed

Static image upload

🧠 Sudoku Solver:

Classic recursive backtracking algorithm

Preserves original puzzle constraints

🎯 Digit Recognition:

CNN model trained on MNIST

High accuracy on handwritten & printed digits

🛠️ Robust preprocessing:

Contour detection

Thresholding

Adaptive thresholding

Digit box enhancement

Warp Perspective 

Noise reduction and centering

💻 Tech Stack
Python

OpenCV (image processing & computer vision)

TensorFlow / Keras (CNN model)

NumPy

Matplotlib

OpenCV VideoCapture (for webcam input)

🧑‍💻 How It Works
🔍 1️⃣ Detecting Sudoku Grid
cv2.findContours() to locate the largest contour (Sudoku grid)

Apply perspective transform to obtain a flat top-down view

🛠️ 2️⃣ Processing Digit Boxes
Grayscale conversion

Gaussian blur

Adaptive thresholding

Morphological transformations

Grid segmentation into 81 cells

🧽 3️⃣ Enhancing Digits for CNN
Centering digit in image

Resizing to 28x28

Noise reduction

Normalization to MNIST format

🧠 4️⃣ CNN Digit Recognition Model
CNN architecture:

Conv2D layers

MaxPooling layers

Dropout

Fully connected Dense layers with softmax

Model saved as .h5 file and loaded at runtime for inference.

📋 5️⃣ Sudoku Solving Algorithm
Implemented recursive backtracking algorithm

Efficiently solves puzzles with constraint checks

🚀 Running the Project
*Clone the github Repository

*Install the dependencies and necesaary techstack

*Run the Final_Sudoku_main.ipynb files.


# MNIST Digit Classification Web Application

This project is a web application that allows users to upload images of handwritten digits and predicts the digit using a Convolutional Neural Network (CNN) trained on the MNIST dataset. The application uses Flask for the web interface and OpenCV for image processing.

## Features

- Upload an image file containing a handwritten digit.
- The application processes the image and uses a pre-trained CNN model to predict the digit.
- Displays the predicted digit on the webpage.

## Technologies Used

- Flask: A micro web framework for Python.
- OpenCV: An open-source computer vision library.
- Keras: An open-source software library that provides a Python interface for artificial neural networks.
- HTML: For the web interface.
- JavaScript: For handling asynchronous requests (AJAX).

## Project Structure

```
├── app.py
├── templates
│   └── index.html
├── uploads
│   └── [uploaded_files]
├── mnist_model.h5
├── requirements.txt
└── README.md
```

- `app.py`: The main Flask application file.
- `templates/index.html`: The HTML file for the web interface.
- `uploads/`: The directory where uploaded images are stored.
- `mnist_model.h5`: The pre-trained CNN model for MNIST digit classification.
- `requirements.txt`: The file listing the Python dependencies.
- `README.md`: The file you are currently reading.

## Prerequisites

- Python 3.x
- Pip (Python package installer)
- OpenCV
- Keras
- TensorFlow (backend for Keras)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/tkmptech/python-cnn-flask.git
   cd python-cnn-flask
   ```

2. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Download or ensure you have the pre-trained MNIST model saved as `mnist_model.h5` in the project directory.

4. Run the application:
   ```sh
   python app.py
   ```

5. Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

1. On the home page, click the "Choose File" button to upload an image of a handwritten digit.
2. Click the "Predict" button to submit the image.
3. The application will process the image, predict the digit, and display the result on the same page.

## Code Explanation

### `app.py`

- `process(file)`: A function that reads the uploaded image file, resizes it to 32x32 pixels, normalizes the pixel values, and inverts the colors to match the MNIST dataset format.
- `index()`: Renders the home page.
- `predict()`: Handles the image upload, saves the file, processes the image, makes a prediction using the CNN model, and renders the result on the home page.

### `templates/index.html`

The HTML file contains the structure of the web interface, including:

- A form to upload an image file.
- A button to submit the image for prediction.
- A section to display the predicted digit.

## Dependencies

- Flask
- OpenCV
- Keras
- TensorFlow
- NumPy
- Matplotlib (optional, for visualization purposes)



## Acknowledgements

- The Keras and TensorFlow teams for providing excellent deep learning tools.
- The MNIST dataset for being a standard benchmark for handwritten digit classification.

Feel free to contribute to this project by submitting issues or pull requests. Enjoy predicting digits!
import os
import cv2
import keras
import os
from flask import Flask, render_template, request
import numpy as np
from matplotlib import pyplot as plt

app = Flask(__name__, static_folder='./templates')


app.config['UPLOADS'] = 'uploads'

cnn = keras.models.load_model('./mnist_model.h5')

def process(file):
    image = cv2.imread(file)
    image = cv2.resize(image, (32, 32))
    image = np.resize(image, (1, 32, 32, 3))
    image = image/255.0
    image = 1-image
    return image

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        filepath = f'uploads/{file.filename}'
        file.save(filepath)
        image = process(filepath)
        print('process done')
        # prediction = cnn.predict_classes(image)
        predict_x=cnn.predict(image)
        # print(predict_x)
        prediction=np.argmax(predict_x,axis=1)
        # print(prediction)
        
        return render_template('index.html', number=prediction[0])

if __name__ == '__main__':
    app.run()
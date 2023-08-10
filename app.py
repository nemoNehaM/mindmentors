#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request
import cv2
import numpy as np

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    image = request.files['select_file']
    image.save('static/file.jpg')
    image = cv2.imread('static/file.jpg')

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

    faces = cascade.detectMultiScale(gray, 1.1, 3)

    for x, y, w, h in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cropped = image[y:y + h, x:x + w]

    cv2.imwrite('static/after.jpg', image)
    try:
        cv2.imwrite('static/cropped.jpg', cropped)
    except:
        pass

    return render_template('predict.html', data="Emotion Prediction Placeholder")

if __name__ == "__main__":
    app.run(debug=True)


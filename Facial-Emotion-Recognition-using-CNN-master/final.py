import streamlit as st
from keras.models import model_from_json
import cv2
import numpy as np

# Load the model from JSON and weights files
json_file = open("C:\\Users\\surya\\Deep Learning\\mod\\Facial-Emotion-Recognition-using-CNN-master\\model.json", 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights("C:\\Users\\surya\\Deep Learning\mod\\Facial-Emotion-Recognition-using-CNN-master\\model.h5")

# Emotion and emoji dictionaries
emotion_dict = {0: "Neutral", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Sad", 5: "Surprised", 6: "Neutral"}
emojis = {0: "😠", 1: "😒", 2: "😨", 3: "😄", 4: "😢", 5: "😲", 6: "😐"}

# Streamlit app
def main():
    st.title("Facial Emotion Recognition App")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = cv2.CascadeClassifier("C:\\Users\\surya\\Deep Learning\\mod\\Facial-Emotion-Recognition-using-CNN-master\\haarcascade_frontalface_default.xml").detectMultiScale(gray, scaleFactor=1.3, minNeighbors=10)
        
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
            
            prediction = model.predict(cropped_img)
            maxindex = int(np.argmax(prediction))
            
            st.image(image, channels="BGR", caption=f"Emotion: {emotion_dict[maxindex]}")
            st.write(f"Emotion: {emotion_dict[maxindex]} {emojis[maxindex]}")

if __name__ == '__main__':
    main()

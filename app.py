import os
import cv2
import numpy as np
import tensorflow as tf
from keras.models import model_from_json
from keras.preprocessing import image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

model = model_from_json(open("C:/Users/usuario/Documents/codigos-vscode/emotions-prova2/fer.json", "r").read())
model.load_weights('C:/Users/usuario/Documents/codigos-vscode/emotions-prova2/fer.h5')
face_haar_cascade = cv2.CascadeClassifier('C:/Users/usuario/Documents/codigos-vscode/emotions-prova2/haarcascade_frontalface_default.xml')


video_path = "C:/Users/usuario/Documents/codigos-vscode/emotions-prova2/emocao.mp4"  # Substitua pelo caminho do seu vídeo
cap = cv2.VideoCapture(video_path)


if not cap.isOpened():
    print("Não foi possível abrir o vídeo")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Não foi possível receber o quadro (fim do vídeo?). Saindo...")
        break

    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces_detected = face_haar_cascade.detectMultiScale(gray_image, 1.32, 5)

    for (x, y, w, h) in faces_detected:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), thickness=7)
        roi_gray = gray_image[y:y+w, x:x+h]
        roi_gray = cv2.resize(roi_gray, (48, 48))

        image_pixels = tf.keras.preprocessing.image.img_to_array(roi_gray)
        image_pixels = np.expand_dims(image_pixels, axis=0)
        image_pixels /= 255

        predictions = model.predict(image_pixels)
        max_index = np.argmax(predictions[0])
        emotion_detection = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
        emotion_prediction = emotion_detection[max_index]

        cv2.putText(frame, emotion_prediction, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

    resize_image = cv2.resize(frame, (1000, 700))
    cv2.imshow('Emotion', resize_image)
    if cv2.waitKey(10) == ord('b'):
        break

cap.release()
cv2.destroyAllWindows()
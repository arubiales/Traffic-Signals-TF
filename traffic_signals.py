import tensorflow as tf
import numpy as np
import pandas as pd
import skimage
import os

sesion = tf.Session()

#Define a function for create the data
def load_data(directory):
    directories = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]

    labels = []
    images = []

    for dir in directories:
        for photo in os.listdir(os.path.join(directory, dir)):
            if photo.endswith('.ppm'):
                images.append(skimage.data.imread(os.path.join(os.path.join(directory, dir), photo)))
                labels.append(int(dir))

    return images, labels

for image in images:
    heigh_mean = []
    width_mean = []
    heigh_mean.append('')

images, labels = load_data('C:/Users/whast/PycharmProjects/pycharm/traffic_signals/BelgiumTSC_Training/Training/')

#a






images, labels = load_data('C:/Users/whast/PycharmProjects/pycharm/traffic_signals/BelgiumTSC_Training/Training')
images
labels



os.listdir('C:/Users/whast/PycharmProjects/pycharm/traffic_signals/BelgiumTSC_Training/Training')
os.path.isdir('C:/Users/whast/PycharmProjects/pycharm/traffic_signals/BelgiumTSC_Training/Training')

#primero en Keras
model = tf.keras.Sequential()

model.add(tf.keras.layers.Dense(units=50, activation='relu', input_shape=[33, 33]))
model.add(tf.keras.layers.Dense(units=100, activation='relu'))
model.add(tf.keras.layers.Dense(units=100, activation='relu'))
model.add(tf.keras.layers.Dense(units=50, activation='relu'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.summary()

model.c































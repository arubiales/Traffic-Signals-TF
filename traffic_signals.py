import tensorflow as tf
import numpy as np
from skimage import transform
import os
from skimage.color import rgb2gray
import skimage.data as imd
import matplotlib.pyplot as plt


from scipy.misc import imread

#Define a function for create the data
# aquí ya tenemos las carpetas
def load_ml_data(data_directory):
    dirs = [d for d in os.listdir(data_directory)
            if os.path.isdir(os.path.join(data_directory, d))]

    labels = []
    images = []

    # ahora vamos a las imagenes
    for d in dirs:
        label_dir = os.path.join(data_directory, d)
        file_names = [os.path.join(label_dir, f)
                      for f in os.listdir(label_dir)
                      if f.endswith('.ppm')]

        for f in file_names:
            images.append(imd.imread(f))
            labels.append(int(d))

    return images, labels


images, labels = load_ml_data('Traffic-Signals-TF/BelgiumTSC_Training/Training')

images = np.array(images)
labels = np.array(images)


images.size








images30 = [transform.resize(image, (30,30)) for image in images]

images30 = np.array(images30)
images30 = rgb2gray(images30)
















































#Lo que no funciona
images40 = [transform.resize(image, (40,40)) for image in images]
images40 = np.array(images40)
images40 = rgb2gray(images40)

labels = np.array(labels)
labels2 = to_categorical(labels)

img_flat = np.ndarray.flatten(images40)
img_flat


#primero en Keras
model=Sequential()

model.add(Dense(128, activation='relu', input_shape=(4575,)))
model.add(Dense(units=256, activation='relu'))
model.add(Dense(units=128, activation='relu'))

model.add(Dense(62, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.summary()

model.fit(images30, labels2, epochs=50, verbose=1)























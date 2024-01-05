#import libraries
import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"]="python"
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
import tensorflow as tf
from tensorflow.python.framework import ops
from PIL import Image

 

# Import Fashion MNIST

fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) \
        = fashion_mnist.load_data() 
 

class_names = ['T-shirt/top', 'Trouser',
        'Pullover', 'Dress', 'Coat',
        'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


train_images = train_images / 255.0

test_images = test_images / 255.0


model = tf.keras.Sequential()
 

model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
model.add(tf.keras.layers.Dense(128, activation='relu' ))
model.add(tf.keras.layers.Dense(10, activation='softmax' ))
 

model.compile(optimizer= tf.optimizers.Adam(),
                      loss='sparse_categorical_crossentropy',
                                    metrics=['accuracy'])
 

model.fit(train_images, train_labels, epochs=50)

 

# test with 10,000 images

test_loss, test_acc = model.evaluate(test_images, test_labels)

 

print('10,000 image Test accuracy:', test_acc)


'''
#run test image from Fashion_MNIST data

img = test_images[15]
img = (np.expand_dims(img,0))
singlePrediction = model.predict(img,steps=1)
print ("Prediction Output")
print(singlePrediction)
print()

NumberElement = singlePrediction.argmax()
Element = np.amax(singlePrediction)


print ("Our Network has concluded that the image number '15' is a "
        +class_names[NumberElement])

print (str(int(Element*100)) + "% Confidence Level")
'''

'''
# read test dress image

imageName = "Dress28x28.JPG"

 

testImg = Image.open(imageName)

testImg.load()

data = np.asarray( testImg, dtype="float" )
 

data = tf.image.rgb_to_grayscale(data)

data = data/255.0

 

data = tf.transpose(data, perm=[2,0,1])
 

singlePrediction = model.predict(data,steps=1)
print ("Prediction Output")
print(singlePrediction)
print()
NumberElement = singlePrediction.argmax()
Element = np.amax(singlePrediction)


print ("Our Network has concluded that the file '"
        +imageName+"' is a "+class_names[NumberElement])

print (str(int(Element*100)) + "% Confidence Level")
'''



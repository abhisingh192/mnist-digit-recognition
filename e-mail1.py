import keras
import tensorflow as tf
import matplotlib as plt


#importing the inbuilt mnist dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()


image_index = 1234
print(y_train[image_index])
plt.imshow(x_train[image_index], cmap='Greys')

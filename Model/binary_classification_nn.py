from data_preprocess import FiducialDataProcess
import ipdb
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import pandas as pd
from tensorflow.keras import optimizers
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.decomposition import NMF

nmf_features  = np.load('nmf_features_type_emot.npy',allow_pickle=True)

x_train_nmf = nmf_features[0]
y_train_cat = nmf_features[1][:,0]   
y_train_emot = nmf_features[1][:,1]   
y_train_emot -= np.ones(len(y_train_emot), dtype='int64')

x_test_nmf = nmf_features [2]
y_test_cat = nmf_features[3][:,0]
y_test_emot = nmf_features[3][:,1]
y_test_emot -= np.ones(len(y_test_emot), dtype='int64')


model = keras.Sequential([
	keras.layers.Dense(96, activation = tf.nn.leaky_relu),
	keras.layers.Dropout(0.4),
	keras.layers.Dense(64, activation = tf.nn.leaky_relu),
	keras.layers.Dropout(0.3),
	keras.layers.Dense(48, activation = tf.nn.leaky_relu),
	keras.layers.Dropout(0.2),
    keras.layers.Dense(2, activation = tf.nn.softmax)
])

model.compile(optimizer = 'adam',
             loss = 'sparse_categorical_crossentropy',
             metrics = ['accuracy'])

history = model.fit(x_train_nmf, y_train_cat, validation_data = (x_test_nmf,y_test_cat), batch_size = 12,epochs = 50)


acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

# Get the number of epochs
epochs = range(len(acc))

model.save('binary_classification_model.h5')

plt.title('Training and validation accuracy')
plt.plot(epochs, acc, color='blue', label='Train')
plt.plot(epochs, val_acc, color='orange', label='Val')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

_ = plt.figure()
plt.title('Training and validation loss')
plt.plot(epochs, loss, color='blue', label='Train')
plt.plot(epochs, val_loss, color='orange', label='Val')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()
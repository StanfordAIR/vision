from __future__ import print_function
from sklearn.model_selection import train_test_split
import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.callbacks import ReduceLROnPlateau
from keras import backend as K
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image as im
import cv2
import random
import numpy as np
import imutils
from PIL import Image
import formatimg

raw_data = pd.read_csv("letters-data/emnist-balanced-train.csv")

train, validate = train_test_split(raw_data, test_size=0.1)

x_train = train.values[:,1:]
y_train = train.values[:,0]

x_validate = validate.values[:,1:]
y_validate = validate.values[:,0]

batch_size = 512
num_classes = 47
epochs = 1

charInd = random.randint(0,10000) # select random index in dataset for testing
emnist = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabdefghnqrt"

img_rows, img_cols = 28, 28

if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
    x_validate = x_validate.reshape(x_validate.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
    x_validate = x_validate.reshape(x_validate.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)

x_train = x_train.astype('float32')
x_validate = x_validate.astype('float32')
x_train /= 255
x_validate /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_validate.shape[0], 'validation samples')

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_validate = keras.utils.to_categorical(y_validate, num_classes)

alphanum = np.where(y_validate[charInd]==1.)[0][0] # get index character in one-hot vector label


# Use data augmentation features of Keras
datagen = ImageDataGenerator(
    width_shift_range = 0.075,
    height_shift_range = 0.075,
    rotation_range = 45,
    shear_range = 0.075,
    zoom_range = 0.05,
    fill_mode = 'constant',
    cval = 0,
    
)

# datagen = ImageDataGenerator(zca_whitening=True)

datagen.fit(x_train)

# Build the model
model = Sequential()
model.add(Conv2D(32, kernel_size=(5, 5),
                 activation='relu',
                 input_shape=input_shape)) # Convolutional layer - 32 filters, 5x5 kernel size
# model.add(Conv2D(32, kernel_size=(3, 3), # Convolutional layer - 32 filters, 3x3 kernel size
#                  activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2))) # max pooling layer - 2x2 pool window size
# model.add(Dropout(0.25)) # dropout layer - sets 1/4 of the neurons to zero
          
# model.add(Conv2D(64, (3, 3), activation='relu'))
# model.add(Conv2D(64, (3, 3), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.5))
 
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

reduce_lr = ReduceLROnPlateau(monitor = 'val_loss', factor = 0.5,
                              patience = 2, min_lr = 0.0001)

# transfer learning
model.load_weights('conv-model.h5')

### comment back in to train ###
# model.fit_generator(datagen.flow(x_train, 
#                                   y_train, 
#                                   batch_size = batch_size), 
#                     epochs = epochs,
#                     verbose = 1,
#                     validation_data = (x_validate, y_validate),
#                     callbacks = [reduce_lr])

score = model.evaluate(x_validate, y_validate, verbose = 0)
# print('Validation loss:', score[0])
# print('Validation accuracy:', score[1])

# serialize model to JSON
model_json = model.to_json()

with open("conv-model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("conv-model.h5")
print("Saved model to disk")

randChar = np.array([x_validate[charInd,:]])

def acnn(img):
  
  ### convert to dataset format ###
  newChar = img
  newChar90 = newChar.rotate(90)
  newChar180 = newChar.rotate(180)
  newChar270 = newChar.rotate(-90)

  newChar = np.array(newChar)/255.
  newChar.reshape(28,28)
  newChar90 = np.array(newChar90)/255.
  newChar90.reshape(28,28)
  newChar180 = np.array(newChar180)/255.
  newChar180.reshape(28,28)
  newChar270 = np.array(newChar270)/255.
  newChar270.reshape(28,28)

  nChar = np.zeros((1,28,28,1))
  for i in range(28):
    for j in range(28):
      nChar[0][i][j][0] = newChar.T[i][j]


  pred0 = model.predict(nChar)

  pred = secondPred = predIndex = secondPredIndex = thirdPred = thirdPredIndex = 0
  o1 = o2 = o3 = "0 deg"

  for i in range(47):
    if pred0[0][i] > pred:
      pred = pred0[0][i]
      predIndex = i

  nChar1 = np.zeros((1,28,28,1))
  for i in range(28):
    for j in range(28):
      nChar1[0][i][j][0] = newChar90.T[i][j]

  pred90 = model.predict(nChar1)

  for i in range(47):
    if pred90[0][i] > pred:
      pred = pred90[0][i]
      predIndex = i
      o1 = "270 deg"

  nChar2 = np.zeros((1,28,28,1))
  for i in range(28):
    for j in range(28):
      nChar2[0][i][j][0] = newChar180.T[i][j]

  pred180 = model.predict(nChar2)

  for i in range(47):
    if pred180[0][i] > pred:
      pred = pred180[0][i]
      predIndex = i
      o1 = "180 deg"

  nChar3 = np.zeros((1,28,28,1))
  for i in range(28):
    for j in range(28):
      nChar3[0][i][j][0] = newChar270.T[i][j]


  pred270 = model.predict(nChar3)

  for i in range(47):
    if pred270[0][i] > pred:
      pred = pred270[0][i]
      predIndex = i
      o1 = "90 deg"

  return [emnist[predIndex], o1]
  # return "1st guess: " + emnist[predIndex]+", rotation "+o1+", probability: " + str(100*pred)+"%"

  # np.reshape(nChar, (28,28))
  # cv2.imshow("random character",np.array(newChar))
  # cv2.waitKey(0)

### 4-hidden-layer Neural Network ###
### Ballpark test accuracy after 1 epoch: 75% ###
### Ballpark time to complete one training epoch and test: 23s ###

import numpy as np
import pandas as pd
import random
import time

import keras as K

m = time.time()

## SET UP DATA ##

train_db = pd.read_csv("data/emnist-balanced-train.csv")
test_db  = pd.read_csv("data/emnist-balanced-test.csv")

charInd = random.randint(0,112000) # select random index in dataset for testing
emnist = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabdefghnqrt"

num_classes = 47
y_train = train_db.iloc[:,0]
y_train = K.utils.np_utils.to_categorical(y_train, num_classes)

x_train = train_db.iloc[:,1:]
x_train = x_train.astype('float32')
x_train /= 255 # normalize training data

alphanum = np.where(y_train[charInd]==1.)[0][0] # get index character in one-hot vector label

## SET UP MODEL ##

inp = K.layers.Input(shape=(784,)) # one neuron for each pixel
hidden_1 = K.layers.Dense(1024, activation='relu')(inp) # use relu activation function for first layer, 1024 neurons
dropout_1 = K.layers.Dropout(0.2)(hidden_1) # use dropout for first layer to increase bias and reduce variance to prevent overfitting, randomly set 1/5 of layer 1 units to zero
hidden_2 = K.layers.Dense(512, activation='relu')(dropout_1) # second layer, relu, 1024 neurons
dropout_2 = K.layers.Dropout(0.2)(hidden_2) # dropout again
out = K.layers.Dense(num_classes, activation='softmax')(hidden_1) # change to hidden_2 with second layer 
model = K.models.Model(outputs=out, inputs=inp)

model.compile(loss='categorical_crossentropy', # cross-entropy loss function, categorical because of softmax
              optimizer='adam', # Adam optimizer function
              metrics=['accuracy']) # report accuracy

model.fit(x_train, y_train, # train the model using the training set
          batch_size=512, epochs=1,
          verbose=1, validation_split=0.05) # carve out 5% data for validation

## TEST/EVALUATE ##

y_test = test_db.iloc[:,0]
y_test = K.utils.np_utils.to_categorical(y_test, num_classes)

x_test = test_db.iloc[:,1:]
x_test = x_test.astype('float32')
x_test /= 255

print(model.evaluate(x_test, y_test, verbose=1)) # evaluate the trained model on the test set

## UTILIZE ##

randChar = np.array([x_train.iloc[charInd,:]])
prediction = model.predict(randChar)
print(prediction)

pred = 0
for i in range(47):
	if prediction[0][i] > pred:
		pred = prediction[0][i]
		print(prediction[0][i])
		predIndex = i

print("Randomly selected test character: "+str(emnist[alphanum]))
print("Model's prediction of this character: " + emnist[predIndex]+", with a probability of " + str(100*pred)+"%")
print("Time to train (s): " + str(time.time() - m))
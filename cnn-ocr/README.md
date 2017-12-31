# Convolutional Neural Network

## Architecture

This CNN has 4 layers:

input layer -> first convolution layer : 5x5x32 -> first max-pooling layer -> second convolution layer : 5x5x64 -> second max-pooling layer -> third fully-connected layer : 1024 nodes -> output layer

## Training

``` $ python mnist_cnn_train.py```

Training logs are saved in "logs/train", and the model is saved in "output".

This directory is designed for augmenting image data we've generated and
training models. It isn't limited to OCR, by any means. If you use the character
images that are in the gen-img-conv-gzip directory (which augments data as
well), you'll see a performance rate at 99.4%-99.7% accuracy after 3 epochs with
current parameters. When I used a dataset with twice as many images (260,000 training, 70,000 testing) and used 5 epochs,
it yielded a model with ~99.9% accuracy.

If you want to see something really cool, enter the command: 

``` $ tensorboard --logdir="model" ```

once you have a trained model!

## Changing the input

This net can be modified for different data input. To do so, edit the params.py file accordingly.

This is based on work from the Tensorflow "Deep MNIST for Experts" (though I'm far from an expert!) - https://www.tensorflow.org/get_started/mnist/pros

and GitHub user hualsuklee - https://github.com/hwalsuklee/tensorflow-mnist-cnn.

JP

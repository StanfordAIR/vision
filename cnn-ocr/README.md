# Convolutional Neural Network

## Architecture

This CNN has 4 layers:

input layer -> first convolution layer : 5x5x32 -> first max-pooling layer -> second convolution layer : 5x5x64 -> second max-pooling layer -> third fully-connected layer : 1024 nodes -> output layer

## Getting Started

To start using this neural network, create a directory called "data" and input your datasets for training and testing, images and labels for both. These should be: 

test-images-idx3-ubyte.gz
test-labels-idx1-ubyte.gz
train-images-idx3-ubyte.gz
train-labels-idx1-ubyte.gz

This is the same format used in the MNIST dataset. If your don't have your data in this format, never fear! Just use grayscaler.py (if your image is RGB) and converter.py in ../gen-img-conv-gzip to get your images into that format.

This net can be modified for different data input. To do so, edit the params.py file accordingly. For instance, it's currently set to accept images of 28x28 size, so imageSize is 28 and imageArea is 784 in params.py. If you want a 30x30 image, imageSize -> 30 and imageArea -> 900.

## Training

``` $ python mnist_cnn_train.py```

Training logs are saved in "logs/train", and the model is saved in "output".

This directory is designed for augmenting image data we've generated and
training models. It isn't limited to OCR, by any means. If you use the character
images that are in the gen-img-conv-gzip directory (which augments data as
well), you'll see a performance rate at 99.4%-99.7% accuracy after 3 epochs with
current parameters. When I used a dataset with twice as many images (260,000 training, 70,000 testing) and used 5 epochs,
it yielded a model with ~99.9% accuracy.

Early trainings took a while on my CPU, so I created a free FloydHub account: https://www.floydhub.com/joshpayne

It's really easy to set one up if you want to train a net on a GPU. Just run

``` $ floyd login ```<br />
``` $ floyd init <project name> ```<br />
``` $ floyd --gpu 'python cnn-train.py' (or test.py or whatever) ```<br />
``` $ floyd logs -t <project id, it tells you what it is> ```<br />
    
    
You only start with 2 hours of GPU time, but it's really easy to create a new account, if you know what I mean. ;)

If you want to see something really cool, enter the command: 

``` $ tensorboard --logdir="model" ```

once you have a trained model!

This is based on work from the Tensorflow "Deep MNIST for Experts" (though I'm far from an expert!) - https://www.tensorflow.org/get_started/mnist/pros

and GitHub user hualsuklee - https://github.com/hwalsuklee/tensorflow-mnist-cnn.

JP

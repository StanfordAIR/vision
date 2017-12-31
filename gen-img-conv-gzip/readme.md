# Image data augmenter, 3 -> 1 channels (grayscale), and gzip converter

generator.py takes in images from the training-template and test-template directories 
and modifies them randomly, generating more data based on the parameters set in the ImageDataGenerator.
This runs on Keras and Tensorflow.

grayscaler.py takes RGB images with 3 channels and converts them to grayscale images with 1 channel.
This runs on OpenCV.

converter.py takes the images in conv-test and conv-train and converts them into numpy arrays before zipping up the labels
and images for each into a .gzip file.

To run everything:
``` $ python generator.py && python grayscaler.py && python converter.py```

For a sanity check, you can also run counter.py at the end.

JP
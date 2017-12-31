This directory is designed for augmenting image data we've generated and
training models. It isn't limited to OCR, by any means. If you use the character
images that are in the gen-img-conv-gzip directory (which augments data as
well), you'll see a performance rate at 99.4%-99.7% accuracy after 3 epochs with
current parameters.

If you want to see something really cool, enter the command: 

``` $ tensorboard --logdir="model" ```

once you have a trained model!

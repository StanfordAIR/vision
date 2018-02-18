# CNN in TensorFlow

Based off of the official Tensorflow MNIST model.

[tf.data](https://www.tensorflow.org/api_docs/python/tf/data),
[tf.estimator.Estimator](https://www.tensorflow.org/api_docs/python/tf/estimator/Estimator),
[tf.layers](https://www.tensorflow.org/api_docs/python/tf/layers)


## Setup

To begin, you'll simply need the latest version of TensorFlow installed.
Then to train the model, run the following:

```
python cnn.py
```

The model will begin training and will automatically evaluate itself on the
validation data.

Illustrative unit tests and benchmarks can be run with:

```
python cnn_test.py
python cnn_test.py --benchmarks=.
```

## Exporting the model

You can export the model into Tensorflow [SavedModel](https://www.tensorflow.org/programmers_guide/saved_model) format by using the argument `--export_dir`:

```
python cnn.py --export_dir ./vs
```

The SavedModel will be saved in a timestamped directory under `./vs` (e.g. `./vs/1513630966/`).

**Getting predictions with SavedModel**
Use [`saved_model_cli`](https://www.tensorflow.org/programmers_guide/saved_model#cli_to_inspect_and_execute_savedmodel) to inspect and execute the SavedModel.

```
saved_model_cli run --dir ./vs/<timestamp> --tag_set serve --signature_def classify --inputs image=<image.npy>
```

To convert your own image(s) to this format, run the following command with your images in this directory:

```
python npcon.py --image <"filename(s)"> --output <"filename(s)"> --batch <True/False>
```


The output should look similar to below:
```
Result for output key classes:
[18]
Result for output key probabilities:
[[   1.31863635e-11    3.33160255e-03    4.68393943e-12    2.98903392e-14
     3.79172548e-07    5.66412202e-15    9.20220983e-20    8.91677772e-08
     7.29750449e-21    1.97541377e-20    3.05716397e-10    1.51980155e-25
     6.33949171e-10    7.35050245e-14    7.62496785e-21    2.95526190e-12
     4.06706855e-21    5.01199837e-09    9.96323705e-01 <- 1.25076656e-06
     1.01232147e-13    9.77554373e-05    3.27998338e-21    7.84026316e-12
     1.61107881e-11    1.56545326e-15    1.30687398e-21    5.33742734e-26
     1.72068582e-07    1.35641665e-10    2.08529087e-07    1.49046433e-23
     1.35477490e-10    2.44773808e-04    6.13433748e-11]]
```

After 12 epochs our augmented 35 class dataset (2000 instances of each class), evaluation accuracy was around ~96%. Predictions were generally good, but some weren't. Likely needs a better dataset.

JP

import numpy as np
import tensorflow as tf

import input_data #mnist...use source from github

mnist = input_data.read_data_sets("data/", one_hot=True)

# images_file = "./emnist-byclass-train-images-idx3-ubyte"
# labels_file = "./emnist-byclass-train-labels-idx1-ubyte"

# def decode_image(image):
#     # Normalize from [0, 255] to [0.0, 1.0]
#     image = tf.decode_raw(image, tf.uint8)
#     image = tf.cast(image, tf.float32)
#     image = tf.reshape(image, [784])
#     print("hi")
#     return image / 255.0

# def decode_label(label):
#     label = tf.decode_raw(label, tf.uint8)  # tf.string -> [tf.uint8]
#     label = tf.reshape(label, [])  # label is a scalar
#     return tf.to_int32(label)

# images = tf.data.FixedLengthRecordDataset(
#       images_file, 28 * 28, header_bytes=16).map(decode_image)
# labels = tf.data.FixedLengthRecordDataset(
#       labels_file, 1, header_bytes=8).map(decode_label)

Xdata_no9 = np.array([x for (x,y) in zip(mnist.train.images,mnist.train.labels) if y[11]==0 or y[12]==0 or y[13]==0 or y[14]==0 or y[15]==0 or y[16]==0 or y[17]==0 or y[18]==0 or y[19]==0 or y[20]==0 or y[21]==0 or y[22]==0 or y[23]==0 or y[24]==0 or y[25]==0 or y[26]==0 or y[27]==0 or y[28]==0 or y[29]==0 or y[30]==0 or y[31]==0 or y[32]==0 or y[33]==0 or y[34]==0 or y[35]==0 or y[36]==0])
ydata_no9 = np.array([y[0:36] for y in mnist.train.labels if y[11]==0 or y[12]==0 or y[13]==0 or y[14]==0 or y[15]==0 or y[16]==0 or y[17]==0 or y[18]==0 or y[19]==0 or y[20]==0 or y[21]==0 or y[22]==0 or y[23]==0 or y[24]==0 or y[25]==0 or y[26]==0 or y[27]==0 or y[28]==0 or y[29]==0 or y[30]==0 or y[31]==0 or y[32]==0 or y[33]==0 or y[34]==0 or y[35]==0 or y[36]==0])

# ma = np.array(images)
# print(ma.shape)

np.save("images-idx", Xdata_no9)
np.save("labels-idx", ydata_no9)
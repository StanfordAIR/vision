import tensorflow as tf
import numpy as np
import os,glob,cv2
import sys,argparse

dir_path = os.path.dirname(os.path.realpath(__file__))
image_path=sys.argv[1] 
filename = dir_path +'/' +image_path
image_size=28
num_channels=1
images = []
# Reading the image using OpenCV
image = cv2.imread(filename, 0)
# Resizing the image to our desired size and preprocessing will be done exactly as done during training
image = cv2.resize(image, (image_size, image_size),0,0, cv2.INTER_LINEAR)
images.append(image)
images = np.array(images, dtype=np.uint8)
images = images.astype('float32')
images = np.multiply(images, 1.0/255.0) 
#The input to the network is of shape [None image_size image_size num_channels]. Hence we reshape.
x_batch = images.reshape(1, image_size, image_size, 1)

# sess=tf.Session()    
# #First let's load meta graph and restore weights
# saver = tf.train.import_meta_graph('data/model.ckpt.meta')
# saver.restore(sess,'data/model.ckpt')

# print [n.name for n in tf.get_default_graph().as_graph_def().node if "Variable" in n.op]

# # Access saved Variables directly
# #       #       print(sess.run('bias:0'))
# # This will print 2, which is the value of bias that we saved


# # Now, let's access and create placeholders variables and
# # create feed-dict to feed new data

# graph = tf.get_default_graph()
# w1 = graph.get_tensor_by_name("w1:0")
# w2 = graph.get_tensor_by_name("w2:0")
# feed_dict ={w1:13.0,w2:17.0}

# #Now, access the op that you want to run. 
# op_to_restore = graph.get_tensor_by_name("op_to_restore:0")

# print sess.run(op_to_restore,feed_dict)
# #This will print 60 which is calculated

sess = tf.Session()
# Step-1: Recreate the network graph. At this step only graph is created.
saver = tf.train.import_meta_graph('model/model.ckpt.meta')
# Step-2: Now let's load the weights saved using the restore method.
saver.restore(sess,'model/model.ckpt')

print [n.name for n in tf.get_default_graph().as_graph_def().node if "Variable" in n.op]

# Accessing the default graph which we have restored
graph = tf.get_default_graph()

# Now, let's get hold of the op that we can be processed to get the output.
# In the original network y_pred is the tensor that is the prediction of the network
y_pred = graph.get_tensor_by_name("y_pred:0")

## Let's feed the images to the input placeholders
x= graph.get_tensor_by_name("x:0") 
y_true = graph.get_tensor_by_name("y_true:0") 
y_test_images = np.zeros((1, 35))



### Creating the feed_dict that is required to be fed to calculate y_pred 
feed_dict_testing = {x: x_batch, y_true: y_test_images}
prediction=tf.argmax(y_pred,0)
with sess.as_default():
	print(prediction.eval(feed_dict={x: x_batch, y_true: y_test_images}))
result=sess.run(y_pred, feed_dict=feed_dict_testing)
# result is of this format [probabiliy_of_rose probability_of_sunflower]
print(result)
# Hello TensorFlow
# Run with: python hello_tensorflow.py
# See http://tensorflow.org
# https://github.com/anujb/HelloTensorflow/master/hello_tensorflow.py 

import tensorflow as tf

# Simple hello world using TensorFlow

# Create a constant op
hello = tf.constant('Hello, TensorFlow!')

# Start tf session
sess = tf.Session()

# Run the op
print(sess.run(hello))

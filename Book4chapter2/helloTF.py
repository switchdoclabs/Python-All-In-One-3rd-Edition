# Python
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"]="python"

import tensorflow as tf



hello = tf.constant('Hello World from TensorFlow')


print(hello)



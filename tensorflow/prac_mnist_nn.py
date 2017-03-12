# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""A very simple MNIST classifier.

See extensive documentation at
http://tensorflow.org/tutorials/mnist/beginners/index.md
"""
#no idea what these for?
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys

from tensorflow.examples.tutorials.mnist import input_data

import tensorflow as tf

FLAGS = None


def main(_):
  # Import data
  mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)
  '''
  mnist.train -55000 with: mnist.train.images mnist.train.labels
  mnist.test -10000 #likewise
  mnist.validation -5000 #likewise
  pixel intensity between 0 and 1
  '''

  # Create the model
  x = tf.placeholder(tf.float32, [None, 784])
  #28x28 None means that a dimension can be of any length
  W = tf.Variable(tf.zeros([784, 10])) #initialize to be zeros
  b = tf.Variable(tf.zeros([10])) #initialize to be zeros, not so good
  y = tf.matmul(x, W) + b #check the dimension of the variables y = x*W + b

  # Define loss and optimizer
  y_ = tf.placeholder(tf.float32, [None, 10]) #one-hot vector

  # The raw formulation of cross-entropy,
  #
  #   tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(tf.nn.softmax(y)),
  #                                 reduction_indices=[1]))
  '''
  reduction_indices = [1] -> the second dimension
  tf.reduce_mean() -> mean over all examples in the batch
  '''
  #
  # can be numerically unstable.
  #
  # So here we use tf.nn.softmax_cross_entropy_with_logits on the raw
  # outputs of 'y', and then average across the batch.
  cross_entropy = tf.reduce_mean(
      tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
  train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
  #learning rate = 0.5

  sess = tf.InteractiveSession()
  tf.global_variables_initializer().run()

  # Train
  for _ in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

  # Test trained model
  correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
  '''
  tf.argmax() -> give the index of the highest entry in a tensor along some axis
  '''
  accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
  '''
  tf.cast() -> [1, 0, 1, 1] to be 0.75
  '''
  print(sess.run(accuracy, feed_dict={x: mnist.test.images,
                                      y_: mnist.test.labels}))

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--data_dir', type=str, default='/tmp/tensorflow/mnist/input_data',
                      help='Directory for storing input data')
  FLAGS, unparsed = parser.parse_known_args()
  tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)

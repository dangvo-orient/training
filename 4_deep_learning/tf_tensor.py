import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = '2'

import tensorflow as tf


# tensor
x = tf.constant(4, shape=(1,1), dtype=tf.float32)
x = tf.ones((3, 3), dtype=tf.int32)
x = tf.zeros((2, 2), dtype=tf.int32)
x = tf.ones_like(x, dtype=tf.float32)
x = tf.fill((2, 3), 10)
x = tf.eye(3, 4)
x = tf.random.normal((3,3), mean=1, stddev=1)
x = tf.random.uniform((1,3), minval=0, maxval=10, dtype=tf.int32)
x = tf.range(1, 10, 2, dtype=tf.int32)
x = tf.cast(x, dtype=tf.float64)

# operation
x = tf.constant([1,2,3])
y = tf.constant([8,6,5])

z = tf.add(x, y)
z = x + y

z = tf.subtract(x, y)
z = x - y

z = tf.multiply(x, y)
z = x * y

z = tf.divide(x, y)
z = x / y

z = tf.pow(x, 2)
z = x ** 2

z = tf.tensordot(x, y, axes=1)
z = tf.reduce_sum(x * y, axis=0)

x = tf.random.normal((2, 3))
y = tf.random.normal((3, 4))
z = tf.matmul(x, y)
z = x @ y

# index
x = tf.range(1, 10, 2)
x = tf.gather(x, [0, 3])

# shape
x = tf.range(6)
x = tf.reshape(x, (2, 3))
x = tf.transpose(x, [1, 0])

print(x)
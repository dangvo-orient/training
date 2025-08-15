
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = '2'

import keras
from keras import layers, regularizers
from keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(-1, 28 * 28).astype("float32") / 255.
x_test = x_test.reshape(-1, 28 * 28).astype("float32") / 255.

# sequential API
model = keras.Sequential(
    [
        keras.Input(shape=(28 * 28,)),
        layers.Dense(512, activation='relu'),
        layers.Dense(256, activation='relu'),
        layers.Dense(10),
    ]
)

# another approach
model = keras.Sequential()
model.add(keras.Input(shape=(28 * 28,)))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dense(10))

# functional approach (more flexible)
inputs = keras.Input(shape=(28 * 28,))
x = layers.Dense(512, activation='relu')(inputs)
x = layers.Dense(256, activation='relu')(x)
outputs = layers.Dense(10, activation='softmax')(x)
model = keras.Model(inputs=inputs, outputs=outputs)

model.summary()

# callbacks
save_callback = keras.callbacks.ModelCheckpoint(
    'checkpoint.weights.h5',
    save_weights_only=True,
    monitor='accuracy',
    save_best_only=False,
)

def scheduler(epoch, lr):
    if epoch < 2:
        return lr
    else:
        return lr * 0.99
lr_scheduler = keras.callbacks.LearningRateScheduler(scheduler, verbose=1)

# custom callback: https://www.tensorflow.org/guide/keras/writing_your_own_callbacks?hl=en

# train
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=False),
    metrics=["accuracy"],
)
model.fit(
    x_train,
    y_train,
    batch_size=32,
    epochs=3,
    verbose=2,
    callbacks=[save_callback, lr_scheduler],
)
model.evaluate(x_test, y_test, batch_size=32, verbose=2)

# save and load model
model.save_weights('saved_model.weights.h5')
model.load_weights('saved_model.weights.h5')

model.save('complete_saved_model.keras')
keras.models.load_model('complete_saved_model.keras')

# other types of layer
layers.Conv2D(64, 3, padding="same", kernel_regularizer=regularizers.l2(0.01))
layers.BatchNormalization()
layers.Dropout(0.6)
layers.SimpleRNN(512, return_sequences=True, activation='relu')
layers.LSTM
layers.GRU
layers.Bidirectional

# custom layer

class LayerOrModelOrBlock(layers.Layer):
    def __init__(self, *args, **kwargs):
        super().__init__()
        ...

    def call(self, input_tensor, training=False):
        ...


# build the model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, TimeDistributed, Dense, GRU
from keras.callbacks import LambdaCallback

model = Sequential([
    Embedding(input_dim=vocab_size, output_dim=50,
              mask_zero=True, trainable=True, input_length=max_seq_len,
              embeddings_initializer=tf.keras.initializers.random_normal()),
    GRU(units=128, return_sequences=True, recurrent_dropout = 0.4),
    TimeDistributed(Dense(units=vocab_size))
])
model.compile(optimizer = 'adam', loss = tf.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])
model.summary()

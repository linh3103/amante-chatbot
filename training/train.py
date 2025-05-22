import tensorflow as tf
import numpy as np
import json

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
import pickle

with open('data.txt', 'r', encoding="utf-8") as f:
    data = json.load(f)

asks = [item["ask"] for item in data]
intents = [item["intent"] for item in data]

oov_token = "<OOV>"
padding_type = "post"

tokenizer = Tokenizer(oov_token=oov_token)
tokenizer.fit_on_texts(asks)
sequences = tokenizer.texts_to_sequences(asks)
padded_sequences = pad_sequences(sequences, padding=padding_type)

label_encoder = LabelEncoder()
labels = label_encoder.fit_transform(intents)
labels = np.array(labels)

vocab_size = len(tokenizer.word_index) + 1
num_classes = len(label_encoder.classes_)

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=16, input_length=padded_sequences.shape[1]),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(num_classes, activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

model.fit(padded_sequences, labels, epochs=10)
model.save('amante_chatbot_model.h5')    

with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle)

def predict(text):
    sequences = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(sequences, maxlen=padded_sequences.shape[1], padding=padding_type)
    prediction = model.predict(padded)[0]
    intent = label_encoder.classes_[np.argmax(prediction)]
    return intent




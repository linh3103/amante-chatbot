from tensorflow.keras.models import load_model
import pickle
import numpy as np

model = load_model('amante_chatbot_model.h5')
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

maxlen = 20  # Adjust this to the maximum length of your input sequences

def predict(text):
    sequences = tokenizer.texts_to_sequences([text])
    padded = tokenizer.padded_sequences(sequences, maxlen=tokenizer.padded_sequences , padding=tokenizer.padding_type)
    prediction = model.predict(padded)[0]
    intent = tokenizer.label_encoder.classes_[np.argmax(prediction)]
    return intent
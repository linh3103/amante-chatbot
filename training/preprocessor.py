import nltk

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Load data
with open('data.txt', 'r', encoding='utf-8') as f:
    raw_data = f.read()

# Preprocess data
def preprocess(data):
    # Tokenize data
    tokens = nltk.word_tokenize(data)
    
    # Lowercase all words
    tokens = [word.lower() for word in tokens]
    
    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]
    
    # Lemmatize words
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    return tokens

print("Preprocessing data...")
processed_data = [preprocess(qa) for qa in raw_data.split('\n') if qa]
print("Data preprocessing complete.")
print("Processed data:", processed_data)
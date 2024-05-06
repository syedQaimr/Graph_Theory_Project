import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer  # Or WordNetLemmatizer for lemmatization

def preprocess_text_file(input_file, target_length=300, output_file=None):

  # Tokenization (split text into words)
  stop_words_set = set(stopwords.words('english'))
  stemmer = PorterStemmer()  # Use PorterStemmer for stemming
  # lemmatizer = WordNetLemmatizer()  # Use WordNetLemmatizer for lemmatization (uncomment if preferred)

  preprocessed_tokens = []
  with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
      tokens = nltk.word_tokenize(line.lower())  # Lowercase and tokenize
      filtered_tokens = [token for token in tokens if token not in stop_words_set]
      stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
      # stemmed_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]  # Uncomment for lemmatization
      preprocessed_tokens.extend(stemmed_tokens)  # Combine tokens from all lines

  # Truncate to target length (optional)
  if target_length and len(preprocessed_tokens) > target_length:
    preprocessed_tokens = preprocessed_tokens[:target_length]

  # Save preprocessed text (optional)
  if output_file:
    with open(output_file, 'w', encoding='utf-8') as f_out:
      f_out.write(' '.join(preprocessed_tokens))

  return preprocessed_tokens

# Example usage
# for i in range(1,14):
input_file = f'Disease/Diseases_Symptoms14.txt'  # Replace with the actual file path
target_length = 300  # Adjust as needed
output_file = f'preprocessed_text14.txt'  # Optional, set to None to skip saving

preprocessed_tokens = preprocess_text_file(input_file, target_length, output_file)
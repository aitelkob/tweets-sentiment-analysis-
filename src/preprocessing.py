# Let's start with the preprocessing part of the project.
# First, we'll create a Python script for cleaning the tweet data.

# The script will include functions to:
# 1. Remove URLs, hashtags, mentions, and special characters from tweets.
# 2. Optionally remove stop words.
# 3. Perform stemming or lemmatization.

import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Ensure that NLTK resources are available
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Function to clean a single tweet
def clean_tweet(tweet, use_stopwords=True, use_stemming=False, use_lemmatization=False):
    # Remove URLs
    tweet = re.sub(r'http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)
    
    # Remove user @ references and '#' from tweet
    tweet = re.sub(r'\@\w+|\#','', tweet)
    
    # Remove punctuations
    tweet = re.sub(r'[^\w\s]', '', tweet)

    # Tokenize tweets
    word_tokens = word_tokenize(tweet)

    # Optionally remove stop words
    if use_stopwords:
        filtered_tweet = [word for word in word_tokens if not word in set(stopwords.words('english'))]
    else:
        filtered_tweet = word_tokens

    # Optionally use stemming
    if use_stemming:
        stemmer = PorterStemmer()
        filtered_tweet = [stemmer.stem(word) for word in filtered_tweet]

    # Optionally use lemmatization
    if use_lemmatization:
        lemmatizer = WordNetLemmatizer()
        filtered_tweet = [lemmatizer.lemmatize(word) for word in filtered_tweet]

    return ' '.join(filtered_tweet)

# Example tweet for testing
example_tweet = "This is an example tweet with a URL http://example.com and some #hashtags and @mentions!"

# Clean the example tweet
cleaned_tweet = clean_tweet(example_tweet, use_stopwords=True, use_stemming=True, use_lemmatization=False)
print(cleaned_tweet)



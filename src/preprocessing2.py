import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Make sure to have these NLTK downloads
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def clean_tweet(tweet, use_stopwords=True, use_stemming=False, use_lemmatization=False):
    # Remove URLs, mentions, and hashtags
    tweet = re.sub(r'http\S+|www\S+|https\S+|\@\w+|\#', '', tweet)
    
    # Remove punctuations
    tweet = re.sub(r'[^\w\s]', '', tweet)

    # Tokenization
    word_tokens = word_tokenize(tweet)

    # Initialize stemmer and lemmatizer
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()

    cleaned_words = []

    for word in word_tokens:
        if use_stopwords and word in stopwords.words('english'):
            continue
        if use_stemming:
            word = stemmer.stem(word)
        if use_lemmatization:
            word = lemmatizer.lemmatize(word)
        cleaned_words.append(word)

    return ' '.join(cleaned_words)

# Example tweet for testing
example_tweet = "This is a better example tweet with a URL http://example.com and some #hashtags and @mentions!"
cleaned_tweet = clean_tweet(example_tweet, use_stopwords=True, use_stemming=True, use_lemmatization=True)
print(cleaned_tweet)


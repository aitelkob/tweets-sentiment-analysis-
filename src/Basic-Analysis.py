import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import nltk
from nltk import ngrams

# Load your dataset
# Load the datasets
positive_tweets = pd.read_csv('data/processedPositive.csv')
neutral_tweets = pd.read_csv('data/processedNeutral.csv')
negative_tweets = pd.read_csv('data/processedNegative.csv')


# Add sentiment labels
positive_tweets['sentiment'] = 'positive'
neutral_tweets['sentiment'] = 'neutral'
negative_tweets['sentiment'] = 'negative'

# Combine the datasets
combined_tweets = pd.concat([positive_tweets, neutral_tweets, negative_tweets], ignore_index=True)

# Shuffle the combined dataset
combined_tweets = combined_tweets.sample(frac=1).reset_index(drop=True)
print(combined_tweets.head())
exit()

# Data Overview
print(tweets_df.info())
print(tweets_df.describe())

# Sentiment Distribution
print(tweets_df['sentiment'].value_counts())

# Tweet Length Analysis
tweets_df['tweet_length'] = tweets_df['tweet_text'].apply(len)
print(tweets_df['tweet_length'].describe())

# Plot tweet length distribution
tweets_df['tweet_length'].hist(bins=50)
plt.show()

# Word Frequency Analysis
all_words = ' '.join(tweets_df['tweet_text']).split()
word_freq = Counter(all_words)
print(word_freq.most_common(10))

# N-gram Analysis
bigrams = ngrams(' '.join(tweets_df['tweet_text']).split(), 2)
bigram_freq = Counter(bigrams)
print(bigram_freq.most_common(10))


import tweepy
from tweepy import OAuthHandler

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import collections

import nltk
from nltk.corpus import stopwords
import re
import networkx

from datetime import datetime

import warnings

warnings.filterwarnings("ignore")

sns.set(font_scale=1.5)
sns.set_style("whitegrid")

consumer_key = 'Twitter Access Keys'
consumer_secret = 'Twitter Access Keys'
access_token = 'Twitter Access Keys'
access_secret = 'Twitter Access Keys'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


# I used a few sites to help aid my in the process but I changed the code to fulfill my needs for this project.
# Sites: Tweepy, Programiz and earthdatascience for pieces and to teach myself the process.

def store(tweet):
    '''
    When connected with twitter this will store any number of tweets it is asked to.
    This program is asked to store 10,000 tweets.
    Parameters:
        tweet: (string) - a tweet imported from twitter.
    Returns:
         stores tweets.
    '''
    print(json.dumps(tweet))
    for tweet in tweepy.Cursor(api.user_timeline).items(10000):
        store(tweet._json)


# searches through all saved tweets to find the ones with the hashtag #blacklivesmatter in them from march 1st 2020.
search_term = "#black+lives+matter -filter:retweets"
tweets = tweepy.Cursor(api.search,
                       q=search_term,
                       lang="en",
                       since='2020-1-03').items()
all_tweets = [tweet.text for tweet in tweets]


def remove_url(text):
    '''
    Removes the url from the text and replaces them nothing to not mess with the word count.
    parameters:
        text: (string) - the text insind of a tweet that you are removing the url from.
    returns:
        The text without the url so the words in the url don't affect the word count.
    '''
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", text).split())


def count():
    '''
    Processes all of the tweets stored that had their urls removed and counts the most common words
    used in each tweet with the hashtag #blacklivesmatter.
    '''
    no_url_tweets = [remove_url(tweet) for tweet in all_tweets]
    no_url_tweets[0].lower().split()
    words_in_tweet = [tweet.lower().split() for tweet in no_url_tweets]
    no_url_words = list(itertools.chain(*words_in_tweet))
    counts_no_urls = collections.Counter(no_url_words)
    counts_no_urls.most_common(15)
    clean_tweets_no_urls = pd.DataFrame(counts_no_urls.most_common(15),
                                        columns=['words', 'count'])

    print(clean_tweets_no_urls.head())


count()



def add_support():
    '''
    This will let the user to create their own tweets. Prints out the username and inputted tweet,
    along with thhe time and date the tweet was created.
    '''
    username = input("Enter your username:")
    your_tweet = input("Enter your tweet:")
    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Your Tweet:")
    print(username)
    print(your_tweet)
    print(date)


add_support()

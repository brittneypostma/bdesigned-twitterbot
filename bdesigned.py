
from os import environ
import time
import tweepy
# import os
# from dotenv import load_dotenv
# load_dotenv()
# from boto.s3.connection import S3Connection

# s3 = S3Connection(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_TOKEN = environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()
print(user.name)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text.encode("utf-8"))


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


# api.update_status('b.Designed Bot is now working! #python #tweepy')


# Narcissist bot
search = '#zerotomastery OR #ztm OR #svelte OR @svelte'
totalItems = 10

for tweet in tweepy.Cursor(api.search, search).items(totalItems):
    try:
        tweet.favorite()  # likes
        tweet.retweet()  # retweets
        print('It worked')
    except tweepy.TweepError as err:
        print(err.reason)
    except StopIteration:
        break

# generous bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     follower.follow()
#     break

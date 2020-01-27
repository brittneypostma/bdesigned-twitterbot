import time
import tweepy
import os
from dotenv import load_dotenv
load_dotenv()


CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
user = api.me()

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
# search = 'python'
# numberOfTweets = 5

# for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
#     try:
#         tweet.favorite() # likes
#         # tweet.retweet() # retweets
#         print('I liked ', tweet.text)
#     except tweepy.TweepError as err:
#         print(err.reason)
#     except StopIteration:
#         break

# generous bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     follower.follow()
#     break

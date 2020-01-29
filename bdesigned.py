from os import environ
import time
import tweepy

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_TOKEN = environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = environ['ACCESS_TOKEN_SECRET']

# # # # TWITTER AUTHENTICATOR # # # #
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()

# # # # TWITTER STREAMER # # # #


class MyStreamListener(tweepy.StreamListener):

     def on_status(self, tweet):
            if not tweet.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
            except Exception as e:
                print("Error on fav", e.reason)
        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                tweet.retweet()
            except Exception as e:
                print("Error on fav", e.reason)


    def on_error(self, status_code):
        if status_code == 420:
            return False
        else:
            print status_code


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

search = ['Python', 'JavaScript', 'WebDev', 'WomenWhoCode', 'MomsCanCode', 'zerotomastery', 'ztm',
          'Zero To Mastery', 'Programmer', 'svelte', 'sveltejs', 'sapper', 'BrittneyPostma', 'b.Designed', 'bDesigned']

myStream.filter(track=search, languages=["en"])


# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text.encode("utf-8"))

# api.update_status('b.Designed Bot is now working! #python #tweepy')

# # # # Limit Handler # # # #
def limit_handler(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)


# # # # generous bot # # # #
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if not follower.following:
        follower.follow()
        print("Now following ", follower.name)


# # # # Narcissist bot # # # #
# search = '#zerotomastery OR #ztm OR #svelte OR @svelte OR #javascript OR #webdev #womenwhocode OR #momscancode OR @WomenWhoCode OR #python OR #programmer @andreineogoie'
# totalItems = 10

# for tweet in tweepy.Cursor(api.search, search).items(totalItems):
#     try:
#         tweet.favorite()  # likes
#         tweet.retweet()  # retweets
#         print('It worked')
#     except tweepy.TweepError as err:
#         print(err.reason)
#     except StopIteration:
#         break

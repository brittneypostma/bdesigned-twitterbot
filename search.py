import tweepy
from config import create_api
import time


def check_mentions(api, keywords, since_id):
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
                               since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            if not tweet.user.following:
                tweet.user.follow()

            sn = tweet.user.screen_name
            api.update_status(status='ZTMBot to the rescue!',
                              in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
    return new_since_id, api


def follow_followers(api):
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            follower.follow()
            print('followed', follower.name)


def fav_retweet(api):
    terms = '#zerotomastery OR #ztm OR #ZTM OR #ZeroToMastery OR #ZerotoMastery OR #svelte OR @svelte OR #javascript OR #webdev #womenwhocode OR #momscancode OR @WomenWhoCode OR #python OR #programmer @andreineogoie'
    for tweet in tweepy.Cursor(api.search, terms).items(100):
        if not tweet.favorited:
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
        print('Liked and retweeted', tweet.text)


def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, ["ZTMBot", "zerotomastery"], since_id)
        follow_followers(api)
        fav_retweet(api)
        print("Waiting...")
        time.sleep(60)


if __name__ == "__main__":
    main()

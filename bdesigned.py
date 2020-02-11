from config import create_api
import time
import tweepy


class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        if tweet.in_reply_to_status_id is not None or \
                tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        if not tweet.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
                print('Liked', tweet.text)
            except Exception as e:
                print("Error on fav", e.reason)
        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                tweet.retweet()
                print('Retweeted', tweet.text)
            except Exception as e:
                print("Error on retweet", e.reason)

    def on_error(self, status_code):
        if status_code == 420:
            return False
        elif status_code == 429:
            time.sleep(60)
            return
        else:
            print(status_code)


def main(keywords, ids):
    api = create_api()
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, follow=ids, languages=["en"])


if __name__ == "___main__":
    track_list = ['Python', 'JavaScript', 'WebDev', 'WomenWhoCode', 'MomsCanCode', 'zerotomastery', 'ztm', 'Zero To Mastery', 'programmer', 'svelte', 'sveltejs', 'sapper', 'BrittneyPostma', 'b.Designed',
                  'bDesigned', 'BrittneyPostma', 'bDesigned', 'syntax', 'syntaxfm', '@syntaxFM', '@stolinski', '@wesbos', '@bDesignedWebDev', '@PostmaBrittney', '#zerotomastery', '#ztm', 'bDesignedWebDev', '@BrittneyPostma']
    # ids = ["224115510"]
    follow_list = [
        '224115510', '815246', '18727585', '733722018596687872', '801833412487184384', '459275531']
    try:
        main(track_list, follow_list)
    except Exception as e:
        print(e.reason)

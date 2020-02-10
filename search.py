import tweepy
from config import create_api
import time

# DO NOT TOUCH LISTS

followed = []

# def check_mentions(api, keywords, since_id):
#     new_since_id = since_id
#     for tweet in tweepy.Cursor(api.mentions_timeline,
#                                since_id=since_id).items():
#         new_since_id = max(tweet.id, new_since_id)
#         print(tweet.id, new_since_id)
#         if tweet.in_reply_to_status_id is not None:
#             continue
#         if any(keyword in tweet.text.lower() for keyword in keywords):
#             if not tweet.user.following:
#                 tweet.user.follow()

#             api.update_status(status='Hi, this is bDesigned-Bot, you can DM this account or reach me through my main account @BrittneyPostma! Thanks! 😀',
#                               in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
#     return new_since_id


def follow_followers(api):
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            follower.follow()
            followed.append(follower.id)
            print('Followed', follower.name)


def unfollow(api):
    for user in followed:
        try:
            if (api.exists_friendship(source_screen_name='@bDesignedWebDev', target_id=user) == False):
                api.destroy_friendship(id=user)
                time.sleep(10)
                followed.remove(user)
                print("Unfollowed:", user)
        except:
            print("Rate Limit Exceeded")
            time.sleep(900)


def fav_retweet(api):
    terms = '#zerotomastery OR #ztm OR #ZTM OR #ZeroToMastery OR #ZerotoMastery OR #svelte OR @svelte OR #javascript OR #webdev #womenwhocode OR #momscancode OR @WomenWhoCode OR #python OR #programmer OR @andreineogoie OR #syntaxFM OR #syntaxfm OR @syntaxFM OR @stolinski OR @wesbos'
    search = tweepy.Cursor(api.search, q=terms,
                           result_type="recent", lang="en").items(25)
    print("Searching for terms...")
    for tweet in search:
        if not tweet.retweeted:
            try:
                tweet.favorite()
                time.sleep(5)
                tweet.retweet()
                print('Liked and retweeted', tweet.text)
            except Exception as e:
                print("Error on fav and retweet", e.message, tweet.text)
        else:
            print("Tweet already liked and retweeted.")


def main():
    api = create_api()
    # since_id = 1
    while True:
        # since_id = check_mentions(api, ["bDesigned", "bdesigned", "BrittneyPostma",
        #                                 "brittneypostma", "Brittney Postma", "b.Designed"], since_id)
        follow_followers(api)
        fav_retweet(api)
        unfollow(api)
        print("Waiting...")
        time.sleep(60)


if __name__ == "__main__":
    main()

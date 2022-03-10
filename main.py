import random
import re
import tweepy
import os
import time
from dotenv import load_dotenv

load_dotenv()

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
LAST_MENTION = os.path.join(THIS_FOLDER, "last_mention.txt")
TWEETS = os.path.join(THIS_FOLDER, "tweets.txt")

with open(TWEETS, "r") as f:
    tweet_library = f.readlines()


def get_last_mention():
    with open(LAST_MENTION, "r") as f:
        return int(f.read().strip())


def update_last_mention(mention_id):
    with open(LAST_MENTION, "w") as f:
        f.write(str(mention_id))


def search(query):
    results = [tweet for tweet in tweet_library if query in tweet]
    if results:
        return random.choice(results)
    return "Nothing to say at the moment."


def reply_to_mentions():
    client = tweepy.Client(
        bearer_token=os.environ.get("BEARER_TOKEN"),
        consumer_key=os.environ.get("CONSUMER_KEY"),
        consumer_secret=os.environ.get("CONSUMER_SECRET"),
        access_token=os.environ.get("ACCESS_TOKEN"),
        access_token_secret=os.environ.get("ACCESS_TOKEN_SECRET")
    )

    me = client.get_me()
    mentions = client.get_users_mentions(
        id=me.data.id,
        since_id=get_last_mention()
    ).data

    if len(mentions) > 0:
        mention_id = 0
        for mention in reversed(mentions):
            mention_id = mention.id
            hashtags = re.findall(r"#(\w+)", mention.text)
            if len(hashtags) > 0:
                query = hashtags[0].replace("#", "")
                result = search(query)
                client.create_tweet(
                    text=result,
                    in_reply_to_tweet_id=mention.id
                )
        update_last_mention(mention_id)

if __name__ == "__main__":
    while True:
        reply_to_mentions()
        time.sleep(60)
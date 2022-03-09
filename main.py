import tweepy
from dotenv import load_dotenv
import os

load_dotenv()

client = tweepy.Client(
    consumer_key=os.environ.get("CONSUMER_KEY"),
    consumer_secret=os.environ.get("CONSUMER_SECRET"),
    access_token=os.environ.get("ACCESS_TOKEN"),
    access_token_secret=os.environ.get("ACCESS_TOKEN_SECRET")
)
client.create_tweet(text="Hello world")
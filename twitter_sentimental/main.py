import tweepy
import configparser

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

# #access tweeys
# public_tweets = api.home_timeline()
# print(public_tweets)

client = tweepy.Client(consumer_key= api_key,consumer_secret= api_key_secret,access_token= access_token,access_token_secret= access_token_secret)
response = client.create_tweet(text='testing api token on v2')
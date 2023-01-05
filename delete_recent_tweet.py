import tweepy


API_KEY = 'xxxxx'
API_KEY_SECRET = 'xxxxx'
BEARER_TOKEN = 'xxxxx'
ACCESS_TOKEN = 'xxxxx'
ACCESS_TOKEN_SECRET = 'xxxxx'


client = tweepy.Client(
    bearer_token = BEARER_TOKEN,
    consumer_key = API_KEY,
    consumer_secret = API_KEY_SECRET,
    access_token = ACCESS_TOKEN,
    access_token_secret = ACCESS_TOKEN_SECRET
)

user = client.get_me()
user_id = user.data.id
tweets = client.get_users_tweets(id=user_id)
recent_tweet = tweets.data[0].id
client.delete_tweet(id=recent_tweet)

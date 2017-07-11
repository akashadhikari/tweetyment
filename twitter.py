import tweepy
from textblob import TextBlob

consumer_key = 'WwpIRHPp7TE3sPpqojWIb0sbk'
consumer_secret = '9u7GZuJXj0g6vtkDu1KEzEGvxOkIrTRu1KiNOlFz2nnZj1RXiM'

access_token = '270245486-XzGX4tMUibrtKIz30fvMSxxEEchWpvJWSN0pLjXJ'
access_token_secret = 'Bpm1k1V2GadyFCLPvHpc19PHSziZ9mBsGPRaRvWOftjfb'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweets = api.search('Syria')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

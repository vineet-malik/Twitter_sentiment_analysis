import tweepy
from textblob import TextBlob 
import pandas as pd 

#authentication (Refer to twitter api for the keys. https://apps.twitter.com/)
consumer_key='<Enter consumer_key from twitter api>'
consumer_secret='<Enter consumer_secret from twitter api>'

access_token='<Enter access_token from twitter api>'
access_token_secret='<Enter access_token_secret from twitter api>'

auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret) 
api=tweepy.API(auth)

#Fetching tweets on the topic
public_tweets=api.search('<Enter Topic>')

#Analysing tweets
d = []
for tweet in public_tweets:
    analysis= TextBlob(tweet.text)
    if analysis.sentiment.polarity >= 0:
    	senti='positive'
    else:
    	senti='negative'
    d.append({'Tweet': tweet.text, 'Sentiment': senti})

df=pd.DataFrame(d)

#Output into a csv file
df.to_csv('output.csv')

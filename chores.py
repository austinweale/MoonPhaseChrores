import os
import tweepy
import twitter
import time
# ALL YOUR SECRET STUFF!
# Consumer Key (API Key)
cons_key = 'eW7wk6JukwBShbsaIW3eChugO'
# Consumer Secret (API Secret)
cons_secret = 'ERBXaB2r4X1Ab9ONCZwqxiVx4r70aiSR0QXhiVeMp8mX5bZHJm'
# Access Token
access_token = '819717437805371400-bvV0j8Rr1FULUmDLyvyfae6Csr3DEGX'
# Access Token Secret
access_token_secret = 'eydOBkLUkxvtCYJWfsFC9kheoPSxDfI1ysHxgbvMkABLD'

auth = tweepy.OAuthHandler(cons_key, cons_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get the current directory's path
dirname = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the book
#book = os.path.join(dirname, 'phase-chores.txt')
# Make your bot read the book!
#tweetbot.read(book)

text_file = open("phase-chores.txt")

lines = text_file.read().split('\n')

for line in lines: 
    api.update_status(line)
    print line
    print '...'
    time.sleep(15) # Sleep for 15 seconds



# Log in to Twitter
#tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)

# Start periodically tweeting
#tweetbot.twitter_tweeting_start(days=0, hours=19, minutes=30, keywords=None, prefix=None, suffix='#PyGaze')

# Use the following to stop periodically tweeting
# (Don't do this directly after starting it, or your bot will do nothing!)
#tweetbot.twitter_tweeting_stop()
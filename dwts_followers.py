#!/usr/bin/env python

import os
import tweepy

consumer_key = os.environ.get('TWITTER_API_KEY')
consumer_secret = os.environ.get('TWITTER_API_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

dwts_couples = [
    ['candacecbure', 'MarkBallas'],
    ['Meryl_Davis', 'MaksimC'],
    ['CharlieaWhite', 'SharnaBurgess'],
    ['jamesmaslow', 'PetaMurgatroyd'],
    ['AmyPurdyGurl', 'derekhough']
]

def follower_count(screen_name):
    user = api.get_user(screen_name)
    return user.followers_count

for couple in dwts_couples:
    couple_followers = 0
    for person in couple:
        followers = follower_count(person)
        couple_followers += followers
        print("{0} has {1} followers".format(person, followers))
    print("Couple {0} has {1} followers".format(couple, couple_followers))
    print("")

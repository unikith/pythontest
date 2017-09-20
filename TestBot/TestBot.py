#!/usr/bin/python
#Base code taken from https://github.com/shantnu/RedditBot/blob/master/Part1/bot_read.py

import praw

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("learnpython")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")

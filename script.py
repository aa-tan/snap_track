import praw
from datetime import datetime
from time import sleep
from configuration import *

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent='owner=ID_UNKNOWN'
)

while(True):
    sleep(60)
    subscribers = reddit.subreddit('thanosdidnothingwrong').subscribers
    with open('population.csv','a') as f:
        now = str(datetime.now())
        f.write("{},{}\n".format(now, subscribers))

import praw
from datetime import datetime
from configuration import *

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent='owner=ID_UNKNOWN'
)

subscribers = reddit.subreddit('thanosdidnothingwrong').subscribers

with open('population.csv','a') as f:
    now = str(datetime.now())
    f.write("{},{}\n".format(now, subscribers))

import praw
from datetime import datetime
import time
from configuration import *

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent='owner=ID_UNKNOWN'
)

starttime=time.time()
while(True):
    with open('population.csv','a') as f:
        subscribers = reddit.subreddit('thanosdidnothingwrong').subscribers
        now = str(datetime.now())
        f.write("{},{}\n".format(now, subscribers))
        time.sleep(60.0 - ((time.time() - starttime) % 60.0))

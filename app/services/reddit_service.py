import praw
from dotenv  import load_dotenv
import os
import pandas as pd
import sqlite3

# Load environmental 
load_dotenv()
REDDIT_SECRET = os.getenv("REDDIT_SECRET") 
REDDIT_ID = client_id = os.getenv("REDDIT_ID")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")
REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")
REDDIT_PW = os.getenv("REDDIT_PW")

# Instantiate reddit conn object
reddit = praw.Reddit(client_id=REDDIT_ID,
                     client_secret=REDDIT_SECRET,
                     password=REDDIT_PW,
                     user_agent=REDDIT_USER_AGENT,
                     username=REDDIT_USERNAME)

# Create a list of top 1000 SFW Subreddits
def subreddit_list():
    df = pd.read_csv('allsubreddits.csv', engine='python', names=['subs','subreddit','nsfw'])
    condition = df['nsfw'] == "nsfw=false"
    df = df[condition]
    df= df.nlargest(1000,'subs')
    listofsubreddits = df['subreddit'].tolist()
    return listofsubreddits

# Create a sqlite3 database of posts from the top 1000 SFW Subreddits
conn = sqlite3.connect("Subredditposts.sqlite3")
curs = conn.cursor()
# sql_command1 = """
# CREATE TABLE subposts (
# title str,
# subreddit str,
# url str,
# body str
# );"""

# curs.execute(sql_command1)

def subwithposts():
    posts = []
    sublist =  subreddit_list()
    for i in sublist:
        testposts = reddit.subreddit(i).hot(limit=1000)#subreddit_list())
        for post in testposts:
            posts.append([post.title, post.subreddit, post.url, post.selftext])
        posts = pd.DataFrame(posts, columns=['title','subreddit','url','body'])
    conn.execute(""" INSERT INTO subposts (title, subreddit, url, body)
    VALUES (?, ?, ?, ?)
    """, posts) 
conn.commit()
conn.close

subwithposts()


# testposts = reddit.subreddit(subreddit_list).hot(limit=10)
# for post in testposts:
#     print(post.title)
# def subredditposts():
#     for submission in reddit.subreddit(subreddit_list['subs']).hot(limit=1000):
#         print(submission.title)
# {
#     post: "test text"
#     predictions: ["subreddit1", "subreddit2", "subreddit3"]
# }

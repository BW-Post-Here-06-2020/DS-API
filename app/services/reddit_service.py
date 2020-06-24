import praw
from dotenv  import load_dotenv
import os
import pandas as pd

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




# Set to read only mode
reddit.read_only = True
# If logged in, should return reddit username
print(reddit.user.me())
print("---")



# Test print ten hot posts on all
for submission in reddit.subreddit("All").hot(limit=10):
    print(submission.title)
    print("---")

# {
#     post: "test text"
#     predictions: ["subreddit1", "subreddit2", "subreddit3"]
# }

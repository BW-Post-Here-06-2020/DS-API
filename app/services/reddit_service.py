import praw
from dotenv import load_dotenv
import os

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

# Set to read only mode
reddit.read_only = True
# If logged in, should return reddit username
print(reddit.user.me())
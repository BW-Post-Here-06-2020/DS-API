import sqlite3

conn = sqlite3.connect("Subredditposts.db")
curs = conn.cursor()
sql_command = """
CREATE TABlE SubPosts{
title str,
subreddit str,
url str,
body str,
};
"""
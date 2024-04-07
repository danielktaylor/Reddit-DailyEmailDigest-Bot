# config.py (for configuring the daily digest bot)
from environs import Env

env = Env()
env.read_env()  # read .env file, if it exists

CLIENT_ID = env("REDDIT_CLIENT_ID")
CLIENT_SECRET = env("REDDIT_CLIENT_SECRET")
USER_AGENT = env("REDDIT_USER_AGENT")
REDDIT_USERNAME = env("REDDIT_USERNAME")
REDDIT_PASSWORD = env("REDDIT_PASSWORD")
MAILJET_API_KEY = env("MAILJET_API_KEY")
MAILJET_SECRET_KEY = env("MAILJET_SECRET_KEY")
TO_EMAIL = env("TO_EMAIL")
FROM_EMAIL = env("FROM_EMAIL")
TEST = env.bool("TEST", False)

SUBREDDITS = env.list("SUBREDDITS")
# Subreddits to fetch from, don't include r/ before the subreddit name. Example: ['science', 'technology', 'maths', 'physics']
TIME_RANGE = env("TIME_RANGE", "day")  # 'day', 'week', 'month', 'year', 'all'
# TIME_RANGE only works for the top.py, controversial.py script.

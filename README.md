# Reddit Daily Email Digest Bot

This project is a fork of [Reddit-DailyEmailDigest-Bot](https://github.com/VenturaFranklin/Reddit-DailyEmailDigest-Bot) in order to Dockerize it. That repo is itself a fork of [Reddit-DailyDigest-Bot](https://github.com/ni5arga/Reddit-DailyDigest-Bot)

**Reddit Daily Email Digest Bot** is a Python bot designed to simplify the process of aggregating and sharing top posts from your favorite subreddits. It fetches the top posts from specified subreddits, compiles them into a neatly formatted daily digest, and automatically emails the digest to an email

## Key Features

- Can create daily digest of top posts from multiple subreddits.
- Fetch top posts from multiple subreddits in the time frame you want.
- Compile the fetched posts into a digest with post details.
- Email the digest to a designated email using mailjet.

## Configuration 
### Reddit API Credentials

Rename the `.env.example` file to `.env` and add your Reddit and Mailjet API credentials. 
 - See [PRAW setup instructions](https://praw.readthedocs.io/en/stable/getting_started/quick_start.html#)
 - See [Mailjet setup instructions](https://github.com/mailjet/mailjet-apiv3-python?tab=readme-ov-file#installation)


### Subreddits 
Modify the `SUBREDDITS` variable in `config.py` to specify the subreddits from which you want to fetch posts. Don't include r/ before the name of the subreddit.

```python
SUBREDDITS = ['science', 'technology', 'maths', 'physics']
```

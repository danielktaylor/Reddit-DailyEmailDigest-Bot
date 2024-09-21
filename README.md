# Reddit Daily Email Digest Bot

This project is a fork of [Reddit-DailyEmailDigest-Bot](https://github.com/VenturaFranklin/Reddit-DailyEmailDigest-Bot) in order to Dockerize it. That repo is itself a fork of [Reddit-DailyDigest-Bot](https://github.com/ni5arga/Reddit-DailyDigest-Bot)

**Reddit Daily Email Digest Bot** is a Python bot designed to simplify the process of aggregating and sharing top posts from your favorite subreddits. It fetches the top posts from specified subreddits, compiles them into a neatly formatted daily digest, and automatically emails the digest to an email

## Key Features

- Can create daily digest of top posts from multiple subreddits.
- Fetch top posts from multiple subreddits in the time frame you want.
- Compile the fetched posts into a digest with post details.
- Email the digest to a designated email using mailjet.

## Setup

### Get API Credentials

* Get a free Reddit API key ([instructions](https://www.jcchouinard.com/reddit-api/))
* Set up a free Mailjet account, and generate an API key

### Configuration
Copy `.env.example` to `.env` and fill out the values

Set the `SUBREDDITS` variable to the subreddit from which you want to fetch posts. Don't include r/ before the name of the subreddit.

## Running

```bash
docker build --tag reddit-digest .
docker run --name=reddit-digest --env-file .env --restart=unless-stopped reddit-digest
```

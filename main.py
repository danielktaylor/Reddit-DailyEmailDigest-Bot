import praw
from datetime import datetime
from urllib.parse import urlparse
from mailjet_rest import Client
import mimetypes
from config import (
    CLIENT_ID,
    CLIENT_SECRET,
    USER_AGENT,
    REDDIT_USERNAME,
    REDDIT_PASSWORD,
    SUBREDDITS,
    TIME_RANGE,
    MAILJET_API_KEY,
    MAILJET_SECRET_KEY,
    TO_EMAIL,
    FROM_EMAIL,
    TEST,
)


def send_email(subject, html):
    # import the mailjet wrapper
    mailjet = Client(auth=(MAILJET_API_KEY, MAILJET_SECRET_KEY), version="v3.1")
    data = {
        "Messages": [
            {
                "From": {"Email": FROM_EMAIL, "Name": FROM_EMAIL},
                "To": [{"Email": TO_EMAIL, "Name": TO_EMAIL}],
                "Subject": subject,
                "HTMLPart": html,
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())


def compile_digest(reddit, test=False):
    for subreddit in SUBREDDITS:
        compiled_content = ""
        submissions = reddit.subreddit(subreddit).top(time_filter=TIME_RANGE)
        for i, submission in enumerate(submissions, start=1):
            if i > 9:
                break

            if submission.is_self:
                text = submission.selftext.replace("\n", "<br />")
            else:
                url = submission.url
                maintype = mimetypes.guess_type(urlparse(url).path)[0]
                if maintype in ("image/png", "image/jpeg", "image/gif"):
                    text = f'<img src="{url}" width="500" height="600">'
                else:
                    text = f'<a href="{url}">{url}</a>'
            date_str = datetime.fromtimestamp(submission.created_utc)
            link = f'<a href="https://www.reddit.com{submission.permalink}">{submission.title}</a>'
            new_content = f"<h2>{i}. {link}</h2><p>{text}</p><p>{submission.score} upvotes; {submission.num_comments} comments; By: by u/{submission.author} on {date_str}<br />{link}</p><br /><hr><br />"
            compiled_content += new_content
        subject = f"{subreddit.title()} {i} Top Posts for {datetime.today().strftime('%Y-%m-%d')}"
        print(subject)
        if not test:
            send_email(subject=subject, html=compiled_content)
        else:
            print(f"THIS IS A TEST: {test}")
            print(compiled_content)
            print("=" * 80)
            print("\n")


if __name__ == "__main__":
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT,
        username=REDDIT_USERNAME,
        password=REDDIT_PASSWORD,
    )
    compile_digest(reddit, test=TEST)

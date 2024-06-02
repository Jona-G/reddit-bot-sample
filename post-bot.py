import random
import praw
import os

reddit = praw.Reddit(client_id=os.getenv('REDDIT_CLIENT_ID'),
                     client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
                     username=os.getenv('REDDIT_USERNAME'),
                     password=os.getenv('REDDIT_PASSWORD'),
                     user_agent=os.getenv('REDDIT_USER_AGENT'))


def post(word):
    subreddit_name = 'subreddit_name'
    subreddit = reddit.subreddit(subreddit_name)
    subreddit.submit(title=word, selftext="")



def get_word(file_path):
    with open(file_path, 'r+') as file:
        content = file.read().strip()
        if content:
            words = content.split()
            if words:
                random_word = random.choice(words)
                words.remove(random_word)
                remaining_content = ' '.join(words)
                file.seek(0)
                file.truncate(0)
                file.write(remaining_content)
                print("Successfully posted the chosen word.")
                return word
            else:
                print("No more words left in the file to post.")
                return ''
        else:
            print("File is empty.")
            return ''

file_path = 'english_words.txt'
word = get_word(file_path)
post(word)

if word:
    print("Today's word:", word)
else:
    print("No word available.")

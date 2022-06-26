class TweetCount:
    def __init__(self, tweet_count, book_id, update_time):
        self.tweet_count = tweet_count
        self.book_id = book_id
        self.update_time = update_time

    def __str__(self):
        return f'tweet_count:{self.tweet_count}, book_id: {self.book_id}, update_time: {self.update_time}'
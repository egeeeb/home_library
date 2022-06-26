class TweetCountRepository:
    def __init__(self, connection):
        self.connection = connection

    UPSERT_SQL = "INSERT INTO home_library.tweet_count(book_id, _count, update_time) " \
                 "VALUES (%s, %s, CURRENT_TIMESTAMP) ON DUPLICATE KEY UPDATE update_time=CURRENT_TIMESTAMP, " \
                 "_count= %s;"

    def upsert(self, tweet_count):
        print(f'TRYING TO INSERT {tweet_count}')
        cursor = self.connection.cursor()
        cursor.execute(self.UPSERT_SQL, (tweet_count.book_id, tweet_count.tweet_count, tweet_count.tweet_count))

        self.connection.commit()

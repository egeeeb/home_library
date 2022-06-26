class GoodreadsGenreRepository:
    def __init__(self, connection):
        self.connection = connection

    INSERT_SQL = "INSERT INTO home_library.goodreads_genres (name, book_id, update_time) " \
                 "VALUES (%s, %s, CURRENT_TIMESTAMP) ON DUPLICATE KEY UPDATE update_time=CURRENT_TIMESTAMP;"

    def insert_all(self, goodreads_genres):
        cursor = self.connection.cursor()
        for goodreads_genre in goodreads_genres:
            cursor.execute(self.INSERT_SQL, (goodreads_genre.name, goodreads_genre.book_id))

        self.connection.commit()

class StatisticsRepository:
    def __init__(self, connection):
        self.connection = connection

    RATINGS_BY_STATUS_SQL = "SELECT ratings.good_reads AS good_reads_rating " \
                            "FROM home_library.books AS books " \
                            "LEFT JOIN home_library.ratings AS ratings ON(books.id = ratings.book_id) " \
                            "WHERE books.status = %s AND ratings.good_reads IS NOT NULL;"

    def read_good_reads_ratings(self):
        cursor = self.connection.cursor()
        cursor.execute(self.RATINGS_BY_STATUS_SQL, ('Read',))
        ratings = []
        for good_reads_rating in cursor:
            ratings.append(good_reads_rating[0])

        return ratings

    def to_read_good_reads_ratings(self):
        cursor = self.connection.cursor()
        cursor.execute(self.RATINGS_BY_STATUS_SQL, ('To-Read',))
        ratings = []
        for (good_reads_rating) in cursor:
            ratings.append(good_reads_rating)

        return ratings

    GENRE_COUNT_SQL = "SELECT genre.name AS genre_name, count(1) AS c " \
                      "FROM home_library.books AS books " \
                      "LEFT JOIN goodreads_genres AS genre ON (books.id = genre.book_id) " \
                      "WHERE genre.name IS NOT NULL GROUP BY genre.name;"

    def genre_count(self):
        cursor = self.connection.cursor()
        cursor.execute(self.GENRE_COUNT_SQL)
        genres = {}
        for (genre_name, c) in cursor:
            genres[genre_name] = c

        return genres

    GENRE_COUNT_BY_STATUS_SQL = "SELECT genre.name AS genre_name, count(1) AS c " \
                                "FROM home_library.books AS books " \
                                "LEFT JOIN goodreads_genres AS genre ON (books.id = genre.book_id) " \
                                "WHERE books.status = %s AND genre.name IS NOT NULL GROUP BY genre.name;"

    def genre_count_by_status(self, status):
        cursor = self.connection.cursor()
        cursor.execute(self.GENRE_COUNT_BY_STATUS_SQL, (status,))
        genres = {}
        for (genre_name, c) in cursor:
            genres[genre_name] = c

        return genres

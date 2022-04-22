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

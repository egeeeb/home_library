from db.rating.rating import Rating


class RatingRepository:
    def __init__(self, connection):
        self.connection = connection

    INSERT_SQL = "INSERT INTO home_library.ratings (good_reads, book_id) VALUES (%s, %s);"

    def insert(self, rating):
        cursor = self.connection.cursor()
        cursor.execute(self.INSERT_SQL, (rating.good_reads, rating.book_id))
        self.connection.commit()

    UPDATE_SQL = "UPDATE home_library.ratings SET good_reads = %s ,update_time = CURRENT_TIMESTAMP WHERE `book_id` = %s;"

    def update(self, rating):
        cursor = self.connection.cursor()
        cursor.execute(self.UPDATE_SQL, (rating.good_reads, rating.book_id))
        self.connection.commit()

    SELECT_BY_ID_SQL = "SELECT book_id, good_reads, update_time FROM home_library.ratings WHERE book_id = %s"

    def get(self, id):
        cursor = self.connection.cursor()
        cursor.execute(self.SELECT_BY_ID_SQL, (id,))
        for (book_id, good_reads, update_time) in cursor:
            cursor.close()
            return Rating(book_id=book_id, good_reads=good_reads, update_time=update_time)

        return None

    def upsert(self, rating):
        current = self.get(rating.book_id)
        if current is None:
            self.insert(rating)
        else:
            self.update(rating)

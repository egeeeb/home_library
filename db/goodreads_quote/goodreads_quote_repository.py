class GoodreadsQuoteRepository:
    def __init__(self, connection):
        self.connection = connection

    UPSERT_SQL = "INSERT INTO home_library.goodreads_quotes(book_id, number_of_quotes, update_time) " \
                 "VALUES (%s, %s, CURRENT_TIMESTAMP) ON DUPLICATE KEY UPDATE update_time=CURRENT_TIMESTAMP, " \
                 "number_of_quotes= %s;"

    def upsert(self, quote):
        print(f'TRYING TO INSERT {quote}')
        cursor = self.connection.cursor()
        cursor.execute(self.UPSERT_SQL, (quote.book_id, quote.noq, quote.noq))

        self.connection.commit()

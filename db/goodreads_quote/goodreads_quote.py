class GoodreadsQuote:
    def __init__(self, book_id, update_time, noq):
        self.book_id = book_id
        self.update_time = update_time
        self.noq = noq

    def __str__(self):
        return f'b_id:{self.book_id} noq:{self.noq} utime: {self.update_time}'

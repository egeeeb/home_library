from db.book import Book


class BooksRepository:
    def __init__(self, connection):
        self.connection = connection

    LIST_SQL = "SELECT * FROM home_library.books"

    def list(self):
        cursor = self.connection.cursor()
        cursor.execute(self.LIST_SQL)
        books = []
        for (id, title, author, publisher, status, owner) in cursor:
            books.append(Book(id, title, author, publisher, status, owner))

        return books

    INSERT_SQL = "INSERT INTO home_library.books (title, author, publisher, status, owner) VALUES (%s, %s, %s, %s, %s);"

    UTF_8 = "SET NAMES 'utf8'; CHARSET 'utf8';"

    def insert(self, book):
        cursor = self.connection.cursor()
        cursor.execute(self.INSERT_SQL, (book.title, book.author, book.publisher, book.status, book.owner))
        self.connection.commit()

    GROUP_COUNT_BY_STATUS_SQL = "SELECT status, count(*) FROM home_library.books GROUP BY status"

    def group_count_by_status(self):
        cursor = self.connection.cursor()
        cursor.execute(self.GROUP_COUNT_BY_STATUS_SQL)
        res = cursor.fetchall()

        return dict(res)

    GROUP_COUNT_BY_PUBLISHER_SQL = "SELECT publisher, count(*) FROM home_library.books GROUP BY publisher"

    def group_count_by_publisher(self):
        cursor = self.connection.cursor()
        cursor.execute(self.GROUP_COUNT_BY_PUBLISHER_SQL)
        res = cursor.fetchall()

        return dict(res)

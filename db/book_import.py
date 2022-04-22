import csv
from db.book import Book


class BookImport:
    def __init__(self, books_repository):
        self.books_repository = books_repository

    def import_from_csv(self, file_name):
        file = open(file_name, encoding='Windows-1254')
        csvreader = csv.reader(file, delimiter=';')
        next(csvreader)

        for row in csvreader:
            print(row)
            book = Book(None, row[0], row[1], row[2], row[3], row[4])
            print(book)
            self.books_repository.insert(book)
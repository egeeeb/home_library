from db.book.book_import import BookImport
from db.book.books_repository import BooksRepository
from db.db_util import DBUtils
from db.goodreads_genre.goodreads_genre import GoodreadsGenre
from db.goodreads_genre.goodreads_genre_repository import GoodreadsGenreRepository
from db.goodreads_quote.goodreads_quote import GoodreadsQuote
from db.goodreads_quote.goodreads_quote_repository import GoodreadsQuoteRepository
from db.rating.rating import Rating
from db.rating.rating_repository import RatingRepository
from db.statistics.statistics import StatisticsRepository
from goodreads_scrape.genre import GoodReadsGenreScraper
from goodreads_scrape.quote import GoodReadsQuoteScraper
from goodreads_scrape.rating import GoodReadsRating
from visuals.bar_chart import BarChart
from visuals.histogram import Histogram
from visuals.pie_chart import PieChart
from visuals.word_cloud import Wordcloud
from datetime import datetime

db_util = None


def create_default_db_util():
    return DBUtils(db_host="localhost", db_port=3306, db_user="admin", db_password="123456", db_name="home_library")


def create_db_util(args):
    return DBUtils(db_host=args[0], db_port=args[1], db_user=args[2], db_password=args[3], db_name=args[4])


def get_db_util():
    global db_util
    if db_util is None:
        db_util = create_default_db_util()
    return db_util


def draw_status_chart():
    conn = get_db_util().create_connection()

    books_repository = BooksRepository(conn)
    PieChart(books_repository.group_count_by_status()).show()

    conn.close()


def draw_publisher_chart(arguments):
    conn = get_db_util().create_connection()

    books_repository = BooksRepository(conn)
    top = int(arguments[0]) if len(arguments) > 0 else None
    BarChart(books_repository.group_count_by_publisher(), top=top).show()

    conn.close()


def import_csv(file_path):
    conn = get_db_util().create_connection()

    books_repository = BooksRepository(conn)
    BookImport(books_repository).import_from_csv(file_path)

    conn.close()


def list():
    conn = get_db_util().create_connection()

    books_repository = BooksRepository(conn)
    books = books_repository.list()
    for book in books:
        print(book)
    conn.close()


def update_goodreads_ratings():
    conn = get_db_util().create_connection()

    books_repository = BooksRepository(conn)
    rating_repository = RatingRepository(conn)
    books = books_repository.list()
    for book in books:
        good_reads_rating = GoodReadsRating(book.title, book.author).rating()
        if good_reads_rating is not None:
            rating = Rating(book_id=book.id, good_reads=good_reads_rating, update_time=None)
            rating_repository.upsert(rating)

        print(f'{book} good_reads rating: {good_reads_rating}')
    conn.close()
    return


def update_goodreads_genres():
    conn = get_db_util().create_connection()

    books_repository = BooksRepository(conn)
    goodreads_genre_repository = GoodreadsGenreRepository(conn)
    books = books_repository.list()
    for book in books:
        good_reads_genre_names = GoodReadsGenreScraper(book.title, book.author).genres()
        book_id = book.id
        good_reads_genres = []
        for good_reads_genre_name in good_reads_genre_names:
            good_reads_genres.append(GoodreadsGenre(good_reads_genre_name, book_id))

        goodreads_genre_repository.insert_all(good_reads_genres)
        print(f'{book} good_reads genre: {good_reads_genre_names}')
    conn.close()
    return


def draw_read_histogram():
    conn = get_db_util().create_connection()
    ratings = StatisticsRepository(conn).read_good_reads_ratings()
    Histogram(ratings).show()
    conn.close()


def draw_to_read_histogram():
    conn = get_db_util().create_connection()
    ratings = StatisticsRepository(conn).to_read_good_reads_ratings()
    Histogram(ratings).show()
    conn.close()


def draw_genre_word_cloud(arguments):
    genres = None
    conn = get_db_util().create_connection()
    if len(arguments) < 1:
        genres = StatisticsRepository(conn).genre_count()
    else:
        genres = StatisticsRepository(conn).genre_count_by_status(arguments[0])
    Wordcloud(genres).show()
    conn.close()

def upgrade_goodreads_quotes():
    print("Working on quotes...")
    conn = get_db_util().create_connection()

    current_time = datetime.now()
    books_repository = BooksRepository(conn)
    books = books_repository.list()
    quote_repository = GoodreadsQuoteRepository(conn)
    for book in books:
        number_of_good_reads_quotes = GoodReadsQuoteScraper(book.title).number_of_quotes()
        goodreads_quote = GoodreadsQuote(book.id, current_time, number_of_good_reads_quotes)
        quote_repository.upsert(goodreads_quote)
    conn.close()
    return


def print_options():
    print("-setup-db host port user password db_name")
    print("-import <filepath>")
    print("-list")
    print("-exit")
    print("-draw-status-chart")
    print("-draw-publisher-chart <top>")
    print("-update-goodreads-ratings")
    print("-update-goodreads-genres")
    print("-draw-read-histogram")
    print("-draw-to-read-histogram")
    print("-genre-distribution-word-cloud <status>")
    print("-fetch-number-of-quotes")

def execute(command, arguments):
    if command == '-import':
        import_csv(arguments[0])
    elif command == '-list':
        list()
    elif command == '-draw-status-chart':
        draw_status_chart()
    elif command == '-draw-publisher-chart':
        draw_publisher_chart(arguments)
    elif command == '-setup-db':
        global db_util
        db_util = create_db_util(arguments)
    elif command == '-update-goodreads-ratings':
        update_goodreads_ratings()
    elif command == '-draw-read-histogram':
        draw_read_histogram()
    elif command == '-draw-to-read-histogram':
        draw_to_read_histogram()
    elif command == '-update-goodreads-genres':
        update_goodreads_genres()
    elif command == '-genre-distribution-word-cloud':
        draw_genre_word_cloud(arguments)
    elif command == '-exit':
        return -1
    elif command == '-fetch-number-of-quotes':
        upgrade_goodreads_quotes()
    return 1


if __name__ == '__main__':
    result = 1
    while result != -1:
        print_options()
        args = input().split(' ')
        result = execute(args[0], args[1:])

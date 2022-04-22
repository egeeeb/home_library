import requests
from bs4 import BeautifulSoup
import difflib


def _similarity(seq1, seq2):
    return difflib.SequenceMatcher(a=seq1.lower(), b=seq2.lower()).ratio()


class GoodReadsRating:
    def __init__(self, book_title, book_author):
        self.book_title = book_title
        self.book_author = book_author

    BASE_URL = "https://www.goodreads.com/search"

    def rating(self):
        page = requests.get(self.BASE_URL, params={'q': self.book_title})
        if page.status_code != 200:
            return None

        body = page.content
        soup = BeautifulSoup(body, 'html.parser')

        book_results = soup.find_all('tr', attrs={'itemtype': 'http://schema.org/Book'})
        if len(book_results) < 1:
            return None

        max_similarity = -1
        rating = None

        for book_result in book_results:
            title_text = book_result.find('a', attrs={'class': 'bookTitle'}).find('span').text
            first_author = book_result.find_all('a', attrs={'class': 'authorName'})[0].find('span').text
            title_similarity = _similarity(title_text, self.book_title)
            author_similarity = _similarity(first_author, self.book_author)

            similarity_score = title_similarity * author_similarity
            if similarity_score > max_similarity:
                rating_text = book_result.find('span', attrs={'class': 'minirating'}).text
                rating = float(rating_text.strip('it was amazing').strip('really').strip('liked it').strip().split(' ')[0])
                max_similarity = similarity_score

        return rating


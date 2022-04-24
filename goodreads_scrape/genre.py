import requests
from bs4 import BeautifulSoup
from goodreads_scrape.util import _similarity

class GoodReadsGenreScraper:
    def __init__(self, book_title, book_author):
        self.book_title = book_title
        self.book_author = book_author

    GOOD_READS_URL = "https://www.goodreads.com"
    BASE_URL = f'{GOOD_READS_URL}/search'


    def _find_best_candidate_link(self):
        page = requests.get(self.BASE_URL, params={'q': self.book_title})
        if page.status_code != 200:
            return None

        body = page.content
        soup = BeautifulSoup(body, 'html.parser')

        book_results = soup.find_all('tr', attrs={'itemtype': 'http://schema.org/Book'})
        if len(book_results) < 1:
            return None

        max_similarity = -1
        best_candidate_link = None

        for book_result in book_results:
            book_link = book_result.find('a', attrs={'class': 'bookTitle'})
            title_text = book_link.find('span').text
            first_author = book_result.find_all('a', attrs={'class': 'authorName'})[0].find('span').text
            title_similarity = _similarity(title_text, self.book_title)
            author_similarity = _similarity(first_author, self.book_author)

            similarity_score = title_similarity * author_similarity
            if similarity_score > max_similarity:
                relative_url = book_link.attrs['href']
                best_candidate_link = f'{self.GOOD_READS_URL}{relative_url}'
                max_similarity = similarity_score

        return best_candidate_link

    def _extract_genre_from_link(self, link):
        page = requests.get(link)
        body = page.content
        soup = BeautifulSoup(body, 'html.parser')

        genre_links = soup.find_all('a', attrs={'class': 'actionLinkLite bookPageGenreLink'})
        genres = set()

        for genre_link in genre_links:
            genre_text = genre_link.text
            genres.add(genre_text)

        return genres

    def genres(self):
        best_candidate_link = self._find_best_candidate_link()
        if best_candidate_link is None:
            return set()

        genres = self._extract_genre_from_link(best_candidate_link)
        return genres


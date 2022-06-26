import requests
from bs4 import BeautifulSoup


class GoodReadsQuoteScraper:
    def __init__(self, book_title):
        self.book_title = book_title

    BASE_URL = "https://www.goodreads.com/search"

    def number_of_quotes(self):
        params = {
            'q': self.book_title,
            'utf8': '✓',
            'search_type': 'quotes'
        }
        page = requests.get(self.BASE_URL, params=params)
        if page.status_code != 200:
            return None
        body = page.content
        soup = BeautifulSoup(body, 'html.parser')

        quote_result = soup.find('h3', attrs={'class': 'searchSubNavContainer'}).text

        noq = self.extract_from_text(quote_result)

        return noq

    def extract_from_text(self, text):
        if text is None:
            return 0

        text_list = text.split()
        if len(text_list) < 4:
            return 0

        total_number = text_list[4]
        return total_number

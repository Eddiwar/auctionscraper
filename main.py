from requests import get;
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import logging
import mysql.connector


class Scraper:

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Healthybow1",
            database="test"
        )
        self.cursor = self.db.cursor()

    def start(self):
        dom = BeautifulSoup(self._get_page('www.google.co.nz'), 'html.parser')

    def _get_page(self, url):
        try:
            with closing(get(url, stream=True)) as resp:
                if self._validate_get_response(resp):
                    return resp.content
                else:
                    return None
        except RequestException as e:
            self.logger.debug(e)

    @staticmethod
    def _validate_get_response(resp):
        content_type = resp.headers['Content-Type'].lower()
        return (resp.status_code == 200
                and content_type is not None
                and content_type.find('html') > -1)


def main():
    scraper = Scraper()
    scraper.start()


if __name__ == '__main__':
    main()



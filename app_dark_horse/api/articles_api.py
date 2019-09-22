import requests

from data_for_test import ARTICLES_URL


class Articles:

    def __init__(self):
        self.articles_url = ARTICLES_URL

    def get_articles(self, data):

        return requests.get(self.articles_url + data)
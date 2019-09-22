import unittest

from api.articles_api import Articles


class TestArticles(unittest.TestCase):

    def setUp(self) -> None:
        self.articles = Articles()

    def test_articles(self):
        response = self.articles.get_articles("1")
        print(response.text)
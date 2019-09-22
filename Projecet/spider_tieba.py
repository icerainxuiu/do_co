

import requests


class TieBaSpider:
    def __init__(self, url):
        self.url = url

    def run(self):
        response = requests.get(self.url)
        text = response.content.decode()
        print(text)


if __name__ == '__main__':
    url = 'http://localhost'
    test_url = TieBaSpider(url)
    test_url.run()
    

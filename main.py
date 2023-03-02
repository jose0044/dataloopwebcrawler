import json

import requests
from bs4 import BeautifulSoup


def create_json_file(json_object):
    with open('results.json', 'w') as jsonFile:
        json.dump(json_object, jsonFile)


def web_crawler(page, weburl):
    json_object = {'results': []}
    if page > 0:
        url = weburl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        for link in s.findAll('div', {'class': 'ipc-media--photo'}):
            image_url = link.get('href')
            json_object['results'].append({
                'imageUrl': image_url,
                'sourceUrl': link,
                'depth': page
            })
    create_json_file(json_object)


if __name__ == '__main__':
    web_crawler(5, 'http://www.imdb.com/title/tt2442560/')

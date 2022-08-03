# -*- coding: UTF-8 -*-
# mypy: ignore-errors
# 개발중일 프로그램입니다.
# 프로그램이 많이 느릴 수 있습니다.

import re, requests
from urllib.parse import urlencode

class Search:
    def __init__(self, link, title):
        self.title: str = title
        self.link: str = f'http://boltmelon.co.kr/text/{link[2:]}'

    def __str__(self):
        return f'Search <title={self.title}, link={self.link}>'

    def __repr__(self):
        return self.__str__()

    def download(self):
        raise NotImplementedError # 추후 추가 예정

class Constants:
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'

def search(title, artist=None, *feat):
    if feat:
        feat = ', '.join(feat)
        feat = f'(feat. {feat})'
    else:
        feat = None
    title = f'{artist or ""} - {title} {feat or ""}'

    response = requests.post('http://boltmelon.co.kr/text/search.php',
        headers={
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': Constants.user_agent,
        },
        data=urlencode({'text': title}),
    )
    text = response.text.strip('\n')
    regex = re.compile(r'(./melon.php\?id=.*?)&(.*?)">', re.IGNORECASE)
    response = regex.findall(text)
    return [Search(*response) for response in response]

# search('파랑', '스월비')[0].download() # 추후 추가 예정

import requests as req

from bs4 import BeautifulSoup


bad_words: ['대통령','고인','노무현','이명박', '박근혜']


url = 'https://namu.wiki/w/%EB%B6%84%EB%A5%98:%EB%94%94%EC%8B%9C%EC%9D%B8%EC%82%AC%EC%9D%B4%EB%93%9C/%EB%B0%88'

res = req.get(url, headers={'User-Agent': 'Mozilla/5.0'})

if res.status_code == 200:
    html = res.text
    soup = BeautifulSoup(html, 'lxml')
    print(soup)
else:
    print(res)
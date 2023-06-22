from bs4 import BeautifulSoup

soup = BeautifulSoup("<p>Some<b>bad<i>HTML")

print(soup.prettify())

print(soup.b)
print(soup.find(text="bad"))
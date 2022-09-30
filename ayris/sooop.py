

from bs4 import BeautifulSoup
import requests 
URL = 'https://www.amazon.de/gp/product/B0756CYWWD/ref=as_li_tl?ie=UTF8&tag=idk01e-21&camp=1638&creative=6742&linkCode=as2&creativeASIN=B0756CYWWD&linkId=868d0edc56c291dbff697d1692708240'
# headers = {"User-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
out=''
# page = requests.get(URL, headers=headers)
# soup = BeautifulSoup(page.content, 'html.parser')
# title = soup.find(id="productTitle").get_text()
# price = soup.find(id="priceblock_ourprice")
# print(soup)
# print(title)
# print(price)
# print(soup.prettify())
# print(soup.title.text.prettify())
# print(soup.title.parent.prettify())
# print(soup.find('div', id='mylist'))
soup = BeautifulSoup(out ,'<div class="wy-nav-shift"></div>')
print(soup.prettify())
# mydivs = soup.findAll('div')
# for div in mydivs: 
#     if (div["class"] == "wy-nav-shift"):
#         print(div)
# tag=soup.b
# print("tag" , tag)
# print(type(tag))
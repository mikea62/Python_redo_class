import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers")

soup = BeautifulSoup(r.content)
print(soup.prettify)

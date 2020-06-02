import requests
from bs4 import BeautifulSoup


f = "https://www.facebook.com/search/people/?q=aviv+yehiel"
result = requests.get(f)
src = result.content
soup = BeautifulSoup(src, features="html.parser")
links = soup.find_all("a")
print(soup.prettify())


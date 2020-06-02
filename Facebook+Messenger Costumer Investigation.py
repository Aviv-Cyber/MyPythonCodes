import requests
from bs4 import BeautifulSoup

class Costumer:
    """ A class to define costumers """
    def __init__(self, first, last, email):
        """ Initialize costumer at first, last, email """
        self.first = first
        self.last = last
        self.email = email

    def fullname(self):
        return '{}{}'.format(self.first, self.last)

    def nameforfacebook(self):
        return '{}{}'.format(self.first, self.last)

    def facebooklookup(self):
        return "https://www.facebook.com/search/people/?q="+(self.first)+"+"+(self.last)

    def scrape(n):
        f = n
        result = requests.get(f)
        src = result.content
        soup = BeautifulSoup(src, features="html.parser")
        links = soup.find_all("a")
        for link in links:
            if "href" in link.attrs:
                print(link.attrs['href'])



cstr_1 = Costumer('aviv', 'yehiel', 'cyberisrael.red@gmail.com')
cstr_2 = Costumer('daniel', 'gold', 'fakedani@gmail.com')
cstr_3 = Costumer('avi', 'cohen', 'avicohen@gmail.com')

costumers = [cstr_1, cstr_2, cstr_3]
for costumer in costumers:
    (Costumer.scrape(Costumer.facebooklookup(costumer)))


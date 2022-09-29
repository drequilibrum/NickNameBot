from bs4 import BeautifulSoup as bs
import requests
import string
import time

let = list(string.ascii_lowercase)

def get_nicks(Tag):
    nicks = []
    for line in Tag:
        nicks.append(line.text)
    return nicks
        
nicks = []
i = 0
for letter in let:
    page = requests.get('http://vnickname.com/letter-' + letter + '.php')
    soup = bs(page.content, "html.parser")
    results = soup.find_all('li', class_ = 'nicknames-list__item nicknames-list__item_block')
    nicks = nicks + get_nicks(results)
    time.sleep(0.2)
    i = i + 1
    print('request {} finished, request status: {}'.format(i,page.status_code) )

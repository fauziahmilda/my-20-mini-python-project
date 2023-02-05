# extract info from website
# send request from our code
# get respond the data we need

from bs4 import BeautifulSoup
import requests

# send request
url = 'http://mildafauziah.blogspot.com/'
r = requests.get(url)

print(f"The url: {url}")
print(f"The response: {r}\n")  # get to know the response is good or not

soup = BeautifulSoup(r.content, 'lxml')
title = soup.find_all('h3', {'class': 'post-title'})
# print(title[0].getText())
print("The articles on that website: ")
x = 0
for item in title:
    print(f"{x+1}. {title[x].getText().strip()}")  # strip for remove newline
    x += 1

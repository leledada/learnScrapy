import requests
from bs4 import BeautifulSoup
from threading import Thread

url = 'https://www.lifeofpix.com/'
rep = requests.get(url)
html = rep.text

soup = BeautifulSoup(html, 'lxml')
links = soup.find_all('div', class_='node large')

authors = {}

for link in links:
    # print(link)
    href = link.find('img', class_='img-low-to-high').get('src')
    file_name = (href.split('/')[-1])
    # print(link.find('a', class_='info').contents)
    # [' ', <img src="https://www.lifeofpix.com/wp-content/uploads/2018/04/IMG_4576-150x150.jpg"/>, ' Daniel\nChen ']
    author = link.find('a', class_='info').contents[-1]
    author = author.strip().split('\n')
    author = ' '.join(author)
    if author in authors:
        authors[author] += 1
    else:
        authors[author] = 1

    pic = requests.get(href, timeout=15)
    tries = 1
    while tries <= 3:
        try:
            with open('pics/' + author + ' ' + str(authors[author]) + ' - ' + file_name, 'wb') as file:
                print(author, authors[author])
                file.write(pic.content)
        except requests.exceptions.RequestException as e:
            tries += 1
            print(e)
            print(href + ' failed')
        else:
            print(href + ' saved')
            break

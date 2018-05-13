import requests

for start in range(0, 250, 20):
    print('fetching', start)
    url = 'https://api.douban.com/v2/movie/top250?start=' + str(start)
    req = requests.get(url)
    data = req.json()
    for movie in data['subjects']:
        print(movie['title'])
import requests

a=requests.get('https://imgs.xkcd.com/comics/python.png')

with open('comic.txt','wb') as f:
    f.write(a.content)

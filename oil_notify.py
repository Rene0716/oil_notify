import urllib.parse
import requests
import bs4

query = urllib.parse.quote_plus('油價格')
# print(query)
url=f'https://www.ptt.cc/bbs/Lifeismoney/search?q={query}'
def get_data(url):
    res=requests.get(url,headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    })
    # print(res.text)
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    title=soup.select('.title a')[2].text
    # print(title)
    return title[5:]

get_data(url)
data=get_data(url)+"\n\n中油小幫手關心您        ´∀`)~♥"
# print(data)
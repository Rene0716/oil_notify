import urllib.parse
import requests
import bs4
import pytest

query = urllib.parse.quote_plus('油價格')
# print(query)
url=f'https://www.ptt.cc/bbs/Lifeismoney/search?q={query}'
def get_data(url:str):
    """
    去ptt省錢版get資料來源
    """
    res=requests.get(url,headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    })
    # print(res.text)
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    title=soup.select('.title a')[2].text
    # print(title)
    return title[5:]

get_data(url)
data=f'{get_data(url)}\n'+' '*13+'中油小幫手~關心您\n'+' '*25+'ξ( ✿＞◡❛)~♥'
# print(data)


def postToLine(token:str,data:str):
    """
    串接line notify api將組好的訊息post到line中
    """
    headers={
        "Authorization":"Bearer "+token,
        "Content-Type":"application/x-www-form-urlencoded"
    }
    payload={'message':data}
    url="https://notify-api.line.me/api/notify"
    
    #Post封包給LINE notify
    resp=requests.post(
        url=url,
        headers = headers,
        params = payload
    )
    print(f'res status:{resp.status_code}')
    print(type(resp))
    return resp
    
token="7n1Fwzn91AoQZc5l7Dam30CYOIJX1Bt3UGpvmrbfYkv"
resp=postToLine(token,data)
print(resp.text)
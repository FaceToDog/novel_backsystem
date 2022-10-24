import requests
import parsel
url = 'http://www.yollewine.com/dongman/index__riben___.html'
header = {
    'Host': 'www.yollewine.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
}
response = requests.get(url=url, headers=header)
# print(response.text)
selector = parsel.Selector(response.text)
media_title = selector.css('.title a::text').getall()
media_url = selector.css('.title a::attr(href)').getall()
print(media_title)
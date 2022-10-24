import re
import requests
import parsel
url = 'https://www.biququ.com/html/6678/'
hard = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.169.400 QQBrowser/11.0.5130.400'
}
a = requests.get(url=url, headers=hard)
# print(a.text)
# unit_a = re.findall('<dd><a href="（.*?）">', a.text)
selector = parsel.Selector(a.text)
novel_title = selector.css('#info h1::text').get()
unit_a = selector.css('#list a::attr(href)').getall()
# print(unit_a)
# print(novel_title)
for i in unit_a:
    unit_url = 'https://www.biququ.com' + i
    # print(unit_url)
    b = requests.get(unit_url, hard)
    selector = parsel.Selector(b.text)
    title = selector.css('.bookname h1::text').get()
    novel = selector.css('#content p::text').getall()
    # print(title)
    # print(novel)
    content = '\n\n'.join(novel)
    # print(novel)
    with open(novel_title + '.txt', mode="a", encoding="utf-8") as f:
        f.write(title)
        f.write('\n')
        f.write(content)
        f.write('\n')
    print(title, "保存成功!")
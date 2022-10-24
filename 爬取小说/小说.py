import re
import requests
import parsel
url = 'https://www.1biqug.com/56/56106/'
hard = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.169.400 QQBrowser/11.0.5130.400'
}
a = requests.get(url=url, headers=hard)
# print(a.text)
unit_a = re.findall('<a style="" href="(.*?)">', a.text)
selector = parsel.Selector(a.text)
novel_title = selector.css('#info h1::text').get()
# print(unit_a)
for i in unit_a:
    unit_url = 'https://www.1biqug.com' + i
    # print(unit_url)
    b = requests.get(unit_url, hard)
    selector = parsel.Selector(b.text)
    title = selector.css('.bookname h1::text').get()
    novel = selector.css('#content::text').getall()
    content = '\n'.join(novel)
    # print(novel)
    with open(novel_title + '.txt', mode="a", encoding="utf-8") as f:
        f.write(title)
        f.write('\n')
        f.write(content)
        f.write('\n')
    print(title, "保存成功!")


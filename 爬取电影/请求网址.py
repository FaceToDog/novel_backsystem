import requests

url = 'https://vod2.bdzybf7.com/share/jgIDxAprjhh98Ebn'
hard = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.169.400 QQBrowser/11.0.5130.400'
}
a = requests.get(url=url, headers=hard)
print(a.text)



# http://www.sxfda.cn/play/872-1-1/
# https://vod2.bdzybf7.com/share/jgIDxAprjhh98Ebn
# https://vod2.bdzybf7.com/html/dplayer/DPlayer.min.js
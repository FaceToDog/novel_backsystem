import requests
import re
# 获得电影地址信息并返回m3u8地址


class VideoUrl:
    def __init__(self, url):
        super(VideoUrl, self).__init__()
        self.url = url
        self.headers = {
            'Connection': 'Keep-Alive',
            'Accept': 'text/html,application/xhtml+xml,*/*',
            'User-Agent': 'Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-m2 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.5.506 UWS/2.10.1.22 Mobile Safari/537.36'
        }

    def request_url(self):
        html = requests.get(self.url).text
        # print(html)
        # compile中的正则
        url_a = re.findall('var player_aaaa=(.*)', html)
        # print(url_a)
        url_b = re.findall('url":"(.*?)"', url_a[0])
        # print(url_b)
        url_c = url_b[0].replace("\\", '')
        # print(url_c)
        html_two = requests.get(url=url_c, headers=self.headers).text
        # print(html_two)
        m3u8_main = re.findall('var main = "(.*?)"', html_two)
        # print(m3u8_main)
        url_html = "https://vod2.bdzybf7.com"
        m3u8_url = url_html + m3u8_main[0]
        index_m3u8 = requests.get(m3u8_url, headers=self.headers).text
        # print(index_m3u8)
        list_content = index_m3u8.split('\n')
        print(list_content)






if __name__ == '__main__':
    get_m3u8 = VideoUrl("http://www.sxfda.cn/play/872-1-1/voddetail/872/")
    get_m3u8.request_url()

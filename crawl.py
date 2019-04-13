import re
import requests
import threading

class Shaoq:
    def __init__(self):
        self.a = []
        self.url = 'http://47.107.142.203:6060/exam'
        self.session = requests.session()
        self.headers = {
                    'Host': '47.107.142.203:6060',
                    'Referer': 'http://47.107.142.203:6060/exam',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
            }

    def get_time(self,txt):
        try:
            tt = re.findall(r'location.href="/exam".*?(\d{3,4})', txt)[0]
            return tt
        except:
            print(txt)

    def start_req(self):
        res = self.session.get(url=self.url, headers=self.headers)
        gt = self.get_time(res.text)
        return gt



    def get_js(self):
        headers = {
            'Host': '47.107.142.203:6060',
            'Referer': 'http://47.107.142.203:6060/exam',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }
        res = self.session.get(url=self.url, headers=headers)
        print(res.text)

    def get_img(self, urll, header):
        self.session.get(url=urll, headers=header)

    def loop(self):
        thread = []
        for i in range(1, 15):
            urll = f'http://47.107.142.203:6060/img/{i}.png'
            header = {"Accept": "image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5",
                     "Accept-Encoding": "gzip, deflate",
                      "Accept-Language": "zh-cn",
                      "Connection": "keep-alive",
                      "Host": "47.107.142.203:6060",
                      "Referer": "http://47.107.142.203:6060/exam",
                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
            t1 = threading.Thread(target=self.get_img, args=(urll, header))
            thread.append(t1)

        for pro in thread:
            pro.start()  # 开始执行线程

if __name__ == '__main__':
    import time
    red = Shaoq()
    tt = red.start_req()
    red.loop()
    time.sleep(int(tt) / 1000)
    red.get_js()

from scrapy import Selector
import requests
import os
import re
import json

url = 'https://movie.douban.com/subject/26425063/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

#创建文件夹
if not os.path.exists('file'):
    os.mkdir('file')

#爬取网页
collect = {}

res = requests.get(url=url, headers=headers)
selector = Selector(text=res.text)
title = selector.xpath('//div[@class="related-info"]/h2/i/text()').extract()
title = re.sub(r'\n+\s+', '', ''.join(title))
overview = selector.xpath('//div[@class="indent"]/span/text()').extract_first().strip()
collect.update({title: overview})
print(collect)
with open('file/crawl.txt', 'wt',encoding='utf-8') as f:
    json.dump(collect,f)
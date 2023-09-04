print('hello world')

import requests

target = "https://www.zhihu.com/question/620452404"
req = requests.get(url=target)
req.encoding = 'utf-8'
print(req.text)


target2 = "https://www.toutiao.com/api/pc/list/feed?channel_id=3189399007&min_behot_time=0&offset=0&refresh_count=1&category=pc_profile_channel&client_extra_params=%7B%22short_video_item%22:%22filter%22%7D&aid=24&app_name=toutiao_web&_signature=_02B4Z6wo00901rLTC7gAAIDB51GAJLjt5zKy9w8AAMhNbRI4BBplKbQaRljKwRJ6TVMolJsGhRzhu-GHHbNdjwSpjp6MEpyqH.8Cjo8PVEC.QnP0XekhVXp5Tf3xhFN.iclglkheuw9PG-sV48"
req2 = requests.get(url=target2)
req2.encoding = 'utf-8'
print(req2.text)


import json

data_dict = json.loads(req2.text)

for news in data_dict['data']:
    print(news['title'])


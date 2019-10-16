from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

import requests


def job():
    # times = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 获取当前时间

    url = "http://wxpusher.zjiecode.com/api/send/message"

    headers_id = {"ContentType": "application/json"}

    data = {
        "appToken": "AT_3MX3lUh6V5TDZDsHbEJgN67pBeT7ZzUy",
        "content": "打卡啦，忘了就等着扣工资啊！！！",
        "contentType": 1,
        # "topicIds": [
        #     1
        # ],
        "uids": [
            "UID_arvlD7cE2jfTQospVS0p7c610aL8"
        ],
        # "url": "http://wxpusher.zjiecode.com"
    }
    r = requests.post(url,headers=headers_id,json=data)
    print(r.text)



scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', day_of_week='0-4', hour=10, minute=34)
scheduler.add_job(job, 'cron', day_of_week='0-4', hour=12, minute=2)
scheduler.add_job(job, 'cron', day_of_week='0-4', hour=12, minute=30)
scheduler.add_job(job, 'cron', day_of_week='0-4', hour=18, minute=17)
scheduler.start()

# {
#   "appToken":"AT_qHT0cTQfLwYOlBV9cJj9zDSyEmspsmyM",
#   "content":"Wxpusher祝你中秋节快乐!",
#   "contentType":1,//内容类型 1表示文字  2表示html 3表示markdown
#   "topicIds":[ //发送目标的topicId，是一个数组！！！
#       123
#   ],
#   "uids":[//发送目标的UID，是一个数组！！！
#       "c1BcpqxEbD8irqlGUh9BhOqR2BvH8yWZ"
#   ],
#   "url":"http://wxpusher.zjiecode.com" //原文链接，可选参数
# }
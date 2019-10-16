from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


import requests


def job():

    times = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(times)

    url = "http://wxmsg.dingliqc.com/send"
    # data = {
    #     "userIds":[
    #         "orPQ808dvkppwJqdhiCalogm0EP0_NXlIEm0Gt"
    #     ],
    #     "template_id":"",
    #     "data":{
    #         "first":{
    #             "value":"打卡",
    #             "color":"#ff0000"
    #         }
    #     }
    # }

    data = "title=提醒打卡&msg="+times+" 打卡啦！！！&userIds=orPQ808dvkppwJqdhiCalogm0EP0_NXlIEm0Gt"
    requests.get(url,data)

# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', day_of_week='0-4', hour=8, minute=40)
scheduler.add_job(job, 'cron', day_of_week='0-4', hour=12, minute=2)
scheduler.add_job(job, 'cron', day_of_week='0-4', hour=12, minute=30)
scheduler.add_job(job, 'cron', day_of_week='0-4', hour=18, minute=17)
scheduler.start()


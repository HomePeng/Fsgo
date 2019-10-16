from wxpy import *

bot = Bot()

# 查找好友
my_friend = bot.friends().search("cloud")[0]

# 发送消息
# 发送文本
my_friend.send("hello")


# 发送图片
# my_friend.send_image("")

embed()

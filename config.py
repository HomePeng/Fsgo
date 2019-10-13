import os

pck_name = "com.fenqile"
lanuch_activity = "com.fenqile.fenqile"
device_name = "192.168.1.4"
wait_timeout = 15
click_post_delay = 0.5
lanuch_time = 5
current_path = os.path.abspath(os.path.dirname(__file__))
screenshot_folder = os.path.join(current_path, "screenshot")
if not os.path.exists(screenshot_folder):
    os.mkdir(screenshot_folder)
    print ("创建截图目录:{}".format(screenshot_folder))

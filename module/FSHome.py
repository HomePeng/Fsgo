import sys, os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from module.Base import Base
import time

# 应用
application = '//*[@resource-id="com.facishare.fs:id/tabLayout"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]'

# 考勤
attendance = '//*[@resource-id="com.facishare.fs:id/id_app_center_top_view"]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]'

# 签到
Check_In = '//*[@text="签到"]'

# 签退
Sign_Off = '//*[@text="签退"]'


class FsHome(Base):
    def __init__(self, driver):
        self.base = Base(driver)

    def appli(self):
        self.base.click(application, "应用")

    def attendance(self):
        self.base.click(attendance, "考勤")

    def CheckIn(self):
        self.base.click(Check_In, "签到")

    def SignOff(self):
        self.base.click(Sign_Off, "签退")

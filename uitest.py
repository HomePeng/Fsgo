import uiautomator2 as u2

d = u2.connect("be2400c")

print(d.info)

d.app_start("com.facishare.fs")

# 点击应用
d.xpath('//*[@resource-id="com.facishare.fs:id/tabLayout"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()

# 点击考勤
d.xpath('//*[@resource-id="com.facishare.fs:id/id_app_center_top_view"]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]').click()

#点击签退
# d.xpath('//*[@resource-id="com.facishare.fs:id/create_check_button"]/android.widget.LinearLayout[1]').click()

# 判断签到是否成功
done = d(resourceId="com.facishare.fs:id/check_time").get_text()
if done == "签到":
    print("签到成功")

# 判断是否需要再签到
# b = d.xpath('//*[@resource-id="com.facishare.fs:id/recheck_btn"]').get_text()
# print(b)

# 再次签到/签到
# d.xpath('//*[@text="签到"]').click()

# 判断签退
d.xpath('//*[@text="12:04 签退"]').get_text()



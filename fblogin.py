from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# 1. Khai bao bien browser
browser  = webdriver.Chrome(executable_path="./chromedriver.exe")

# 2. Mở thử một trang web
browser.get("http://facebook.com")


# 2a. Điền thông tin vào ô user và pass

txtUser = browser.find_element("id", "email")
txtUser.send_keys("photosuploader39@gmail.com") 

txtPass = browser.find_element("id", "pass")
txtPass.send_keys("Trang.nk123") 

# 2b. Submit form

txtPass.send_keys(Keys.ENTER)


# 3. Dừng chương trình 5 giây
sleep(10)

# 4. Đóng trình duyệt
browser.close()
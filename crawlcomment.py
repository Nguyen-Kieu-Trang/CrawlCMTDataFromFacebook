from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


# 1. Khai bao bien browser
browser  = webdriver.Chrome(executable_path="./chromedriver.exe")

# 2. Mở URL của post
browser.get("https://www.facebook.com/CafeF/posts/pfbid02mgbmJ4MiJauva8k1UMRc8ofMgE7tFi4BovHQ8H5onjCCRYtFF2eX22m4AtVepwFpl")

sleep(5)

# 3. Lấy link hiện comment
# showcomment_link = browser.find_element("xpath","/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[4]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/span/div/div/div[2]/i")
showcomment_link = browser.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/div[1]/div/div[3]/span[1]/a")

showcomment_link.click()
sleep(5)

# 4. Lấy comment
# /html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div[2]/div[3]/div[2]/div/a
showmore_link = browser.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div[2]/div[3]/div[2]/div/a")
showmore_link.click()
# # sleep(random.randint(5,10))
sleep(7)
# showmore_link.click()
# sleep(7)
# showmore_link.click()
# sleep(7)
# showmore_link.click()
# sleep(7)
# showmore_link.click()
# sleep(7)

# 5. Tìm tất cả các comment và ghi ra màn hình (hoặc file)
# -> lấy all thẻ div có thuộc tính aria-label='Bình luận'

comment_list = browser.find_elements("xpath","//div[@aria-label='Comment']")
# print(comment_list)
# Lặp trong tất cả các comment và hiển thị nội dung comment ra màn hình

for comment in comment_list:
    # hiển thị tên người và nội dung, cách nhau bởi dấu :
   #  poster = comment.find_element("class name","_6qw4")
    content = comment.find_element("class name", "_3l3x")
   #  print("*", poster.text,":", content.text)
    print("*", content.text)


# sleep(5)

# 6. Đóng browser
browser.close()
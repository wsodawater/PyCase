import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class Testweixin:

    def setup(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_addressm = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def teardown(self):
        self.driver.quit()

    def test_cookie(self):
            # 获取cookie 并储存
        # self.driver.get("https://work.weixin.qq.com/")
        # self.driver.find_element(By.XPATH, "//*[@id='indexTop']/div[2]/aside/a[1]").click()
        # sleep(15)
        # cookies = self.driver.get_cookies()
        # with open("cookie.json","w") as f:
        #     json.dump(cookies,f)

        self.driver.get("https://work.weixin.qq.com/")
            # 读取cookie
        with open("cookie.json","r") as f:
            cookies = json.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.XPATH, "//*[@id='menu_customer']/span").click()
        sleep(5)





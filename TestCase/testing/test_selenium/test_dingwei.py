from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_dingwei():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_baidu(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.CSS_SELECTOR,"#kw").send_keys("baidu")
        self.driver.find_element(By.CSS_SELECTOR,"#su").click()

from time import sleep

from selenium import webdriver

class Testwindows():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_windows(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.window_handles)
        print(self.driver.current_window_handle)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        print(self.driver.window_handles)
        print(self.driver.current_window_handle)

        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("weiwei")
        self.driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys("password")
        print(self.driver.window_handles)
        print(self.driver.current_window_handle)
        sleep(3)

        self.driver.switch_to.window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("weiwei")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("123456")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()

        sleep(3)




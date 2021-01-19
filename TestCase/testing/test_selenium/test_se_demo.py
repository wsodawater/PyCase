from selenium import webdriver

#创建测试类
class Testhogwards():
    #创建测试方法
    def setup(self):
        #初始化环境，初始化driver
        self.driver = webdriver.Chrome()
        #窗口最大化
        self.driver.maximize_window()
        # 隐式等待(全局)
        self.driver.implicitly_wait(5)

    def teardown(self):
        #退出，资源回收
        self.driver.quit()

    def test_hogwards(self):
        #打开被测网址
        self.driver.get("https://testerhome.com/")
        #定位元素
        self.driver.find_element_by_link_text("跳过").click()
        self.driver.find_element_by_link_text("社团").click()





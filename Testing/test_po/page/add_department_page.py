from selenium.webdriver.common.by import By

from Testing.test_po.page.base_page import BasePage
from Testing.test_po.page.contact_page import ContactPage


class AddPeartmentPage(BasePage):

    def add_deartment(self):
        self.driver.find_element_by_css_selector(
            ".qui_dialog_body.ww_dialog_body [class='qui_inputText ww_inputText']").send_keys("部门名")
        self.driver.find_element_by_css_selector(".js_parent_party_name").click()
        self.driver.find_element_by_css_selector(
            ".qui_dialog_body.ww_dialog_body [id='1688850780039479_anchor']").click()
        self.driver.find_element_by_xpath("//*[@id='__dialog__MNDialog__']/div/div[3]/a[1]").click()

        return ContactPage()
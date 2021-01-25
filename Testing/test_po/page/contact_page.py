from selenium.webdriver.common.by import By

from Testing.test_po.page.add_department_page import AddPeartmentPage
from Testing.test_po.page.base_page import BasePage


class ContactPage(BasePage):

    def goto_add_deparment(self):
        self.driver.find_element(By.XPATH, "//*[@id='js_contacts12']/div/div[1]/div/div[1]/a/i").click()
        self.driver.find_element(By.XPATH, "//*[@id='js_contacts12']/div/div[1]/ul/li[1]/a").click()
        return AddPeartmentPage()

    def get_list(self):

        self.driver.find_element_by_xpath('//*[@id="memberSearchInput"]').send_keys("部门名")
        department_list = self.driver.find_elements_by_id("search_party_list")
        department_lists = []
        for i in department_list:
            department_lists.append(i.text)

        return department_lists



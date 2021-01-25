from Testing.test_po.page.contact_page import ContactPage
from Testing.test_po.page.base_page import BasePage



class MemberPage(BasePage):

    def add_department(self):
        return ContactPage()

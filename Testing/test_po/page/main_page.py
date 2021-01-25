from Testing.test_po.page.add_department_page import AddPeartmentPage
from Testing.test_po.page.add_member_page import MemberPage
from Testing.test_po.page.base_page import BasePage


class MainPage(BasePage):

    def goto_contact(self):
        return AddPeartmentPage()

    def goto_add_member(self):
        return MemberPage()


from Testing.test_po.page.contact_page import ContactPage
from Testing.test_po.page.main_page import MainPage


class TestAddDeartment():

      def seatup(self):
          self.main = MainPage()
          self.contact =  ContactPage()

      def test_add_deartment(self):
          main = MainPage()
          result = main.goto_contact().add_deartment().get_list("部门名")
          assert "部门名" in result


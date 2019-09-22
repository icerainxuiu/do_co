from base.base_driver import get_driver
from page.contacts_page import ContactsPage


class TestContact:
    def setup(self):
        self.driver = get_driver()
        self.page = ContactsPage(self.driver)

    def teardown(self):
        self.driver.quit()


    def test_contact(self):
        self.page.click_add_contact()
        self.page.input_name("李白")
        self.page.input_phone("13222")

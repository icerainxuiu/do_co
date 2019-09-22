from selenium.webdriver.common.by import By

from base.base_action import Action


class ContactsPage(Action):
    # 添加联系人按钮
    add_contact_btn = By.ID, "com.android.contacts:id/floating_action_button"
    name_contact = By.XPATH, '//*[@text="姓名"]'
    phone_contact = By.XPATH, '//*[@text="电话"]'

    def click_add_contact(self):
        self.click_element(self.add_contact_btn)

    def input_name(self, content):
        self.input_text(self.name_contact, content)

    def input_phone(self, content):
        self.input_text(self.phone_contact, content)

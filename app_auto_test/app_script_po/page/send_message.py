from selenium.webdriver.common.by import By

from base.base_action import Actions


class MessagePage(Actions):

    # com.android.mms:id/action_compose_new
    # com.android.mms:id/recipients_editor
    # com.android.mms:id/send_button_sms
    # com.android.mms:id/embedded_text_editor
    write_message_btn = By.ID, 'com.android.mms:id/action_compose_new'
    phone = By.ID, 'com.android.mms:id/recipients_editor'
    send_message_btn = By.ID, 'com.android.mms:id/send_button_sms'
    message = By.ID, 'com.android.mms:id/embedded_text_editor'

    def click_write_btn(self):
        self.click_btn(self.write_message_btn)

    def send_content(self, content):
        self.send_message(self.phone, content)

    def click_send(self):
        self.click_btn(self.send_message_btn)

    def send_msg(self, content):
        self.send_message(self.message, content)
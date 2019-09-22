from page.send_message import MessagePage


class Page:
    def __init__(self, driver):
        self.driver = driver

    @property
    def message_page(self):
        return MessagePage(self.driver)



# class People:
#     def __init__(self, name):
#         self.name = name
#         print(self.name)
#
# xiaoming = People("xiaoming")

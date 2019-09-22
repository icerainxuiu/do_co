from day6_web.v3.utils_po import DriverUtils


class BasePage(object):
    # ����������࣬������������������
    # ��װ��ʼ���������������������ʵ��
    def __init__(self):
        self.driver = DriverUtils.get_driver()

    # �������������Ѱ��Ԫ�صķ������������ҵ���Ԫ��
    # location ���ݵ���һ��Ԫ�飬������Ѱ�Ҷ�����Ҫ��������
    # ���Լ� * ���������
    def find_element(self, location):
        return self.driver.find_element(*location)


class BaseHandle(object):
    # �����������࣬��װ��������
    # �Լ������ı�����
    # ���ݵ���������δԪ�ض����Ҫ������ı�
    # @staticmethod
    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)


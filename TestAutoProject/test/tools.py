# 系统菜单
import pymysql


def card_menu():
    print('*' * 30)
    print("请输入你的操作：\n"
          "1. 添加成员:\n"
          "2. 查看全部:\n"
          "3. 删除成员:\n"
          "4. 修改成员:\n"
          "0. 退出系统")
    print("*" * 30)


# 创建链接数据库类、
class ConnectCardSQL(object):
    _conn = None

    # 链接数据库方法
    @classmethod
    def connect_card(cls):
        if cls._conn is None:
            cls._conn = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                password='root',
                database='test',
                charset='utf8')
        return cls._conn.cursor()

    @classmethod
    def quit_connect(cls):
        if cls._conn:
            cls._conn.cursor().close()
            cls._conn.close()
            cls._conn = None


class CardProxy(object):
    # 初始化操作对象，创建链接数据库对象
    def __init__(self):
        self.card_con = ConnectCardSQL().connect_card()

    # 退出数据库，断开链接
    def __del__(self):
        ConnectCardSQL().quit_connect()

    # 显示全部数据库成员
    def show_card(self):
        self.card_con.execute('select * from carder;')
        data_list = self.card_con.fetchall()
        print(data_list)

    # 添加成员进数据库
    def add_card(self, email, user_name, qq_num, gender):
        self.card_con.execute('insert into carder values(0,{},{},{},{})'.format(email, user_name, qq_num, gender))


# 创建操作类使用对象，操作数据库的增删查找方法


if __name__ == '__main__':
    card_menu()
    proxy = CardProxy()
    proxy.add_card(email='39393993@qq.com', user_name='zhangsan', qq_num='324234234', gender='男')


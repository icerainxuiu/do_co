from pymysql import connect, Connection


class DBUtil:

    # 初始化方法，实例对象需要传入的参数，有域名，端口，用户名，密码，数据库，字符集
    def __init__(self, host, port, user, password, database, charset):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.conn = None
        self.cur = None

    def get_conn(self):  # 创建获取连接方法
        self.conn = Connection(host=self.host,
                               port=self.port,
                               user=self.user,
                               password=self.password,
                               database=self.database,
                               charset=self.charset)
        return self.conn  # 将连接对象返回

    def get_cur(self):  # 创建获取游标方法
        self.cur = self.get_conn().cursor()
        return self.cur  # 将游标对象返回

    def close_scr(self):
        if self.cur:  # 如果游标是空就不执行
            self.cur.close()  # 非空就关闭
            self.cur = None  # 并重置属性为None
        if self.conn:
            self.conn.close()
            self.conn = None

#
# conn = connect(host="localhost", port=3306, user="root", password='root', database="books", charset='utf8')
# cur = conn.cursor()
#
# cur.close()
# conn.close()


if __name__ == '__main__':
    util = DBUtil("localhost", 3306, "root", "root", "books", charset="utf8")
    conn = util.get_conn()
    cur = util.get_cur()
    sql = "select * from t_book"
    cur.execute(sql)
    # cur.execute(sql)
    data = cur.fetchall()
    print(data)

    util.close_scr()

from pymysql import connect


class DBUtil:

    def __init__(self, host, port, user, password, database, charset):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.conn = None
        self.cur = None

    def get_conn(self):
        self.conn = connect(host=self.host,
                            port=self.port,
                            user=self.user,
                            password=self.password,
                            database=self.database,
                            charset=self.charset)
        return self.conn

    def get_cur(self):
        return self.get_conn().cursor()

    def close_scr(self):
        if self.cur:
            self.get_cur().close()
            self.cur = None
        if self.conn:
            self.get_conn().close()
            self.conn = None


if __name__ == '__main__':
    util = DBUtil("localhost",3306,"root","root","books","utf8")
    conn = util.get_conn()
    cur = util.get_cur()
    sql = "select * from t_book"
    cur.execute(sql)
    print("影响的行数", cur.rowcount)
    data = cur.fetchall()
    print(data)
    util.close_scr()


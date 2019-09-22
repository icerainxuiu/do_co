import pymysql

conn = pymysql.connect(host="localhost", port=3306, user="root", password='root', database="books", charset='utf8')
cur = conn.cursor()
sql = "select * from t_book;"
cur.execute(sql)
data = cur.fetchone()
# print(data)
print(cur.fetchmany())
# print(cur.fetchmany(5))
# cur.rowcount()
# data = cur.fetchmany(3)
# data = cur.fetchone()

# print(data)
cur.close()
conn.close()

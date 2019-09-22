import pymysql

conn = pymysql.connect(host="localhost", port=3306, user="root", password="root", database="books", charset="utf8", autocommit=True)
cur = conn.cursor()
sql = "insert into t_book values('4', '西游记', '1977-09-01', '58', '4534', 0);"
cur.execute(sql)
print(cur.rowcount)
sql = "select * from t_book;"
cur.execute(sql)
print(cur.fetchall())
cur.close()
conn.close()
from pymysql import connect

conn = connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    database='books',
    charset='utf8')
cur = conn.cursor()
try:

    sql = 'insert into t_book values(6, "三国演义", "1977-4-4", "45634", "34535", 0)'
    cur.execute(sql)
    sql1 = "insert into t_hero values(7, '吕布', '1','三姓家奴', '0', '6')"
    cur.execute(sql1)
    conn.commit()
except Exception as e:
    conn.rollback()
    print(e)
cur.close()
conn.close()
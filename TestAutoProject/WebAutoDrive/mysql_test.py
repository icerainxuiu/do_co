from pymysql import *


def main():
    conn = connect(host='localhost', port=3306,user='root',password='root',database='jing_dong',charset='utf8')
    cur = conn.cursor()
    cur.execute("select * from goods;")
    print(cur.fetchall())
    data_list = list()
    for data in cur.fetchall():
        data_list.append(data)
    print(data_list)
    cur.close()
    conn.close()

if __name__ == '__main__':

    main()
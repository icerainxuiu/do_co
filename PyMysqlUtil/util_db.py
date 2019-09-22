# import pymysql
#
#
# class DBUtil:
#     # conn = None
#     # cur = None
#
#     @classmethod
#     def get_conn(
#             cls,
#             host,
#             user,
#             password,
#             database,
#             charset='utf8',
#             port=3306):
#         conn = pymysql.connect(
#             host=host,
#             user=user,
#             password=password,
#             database=database,
#             charset=charset,
#             port=port)
#         return conn
#
#     @classmethod
#     def get_cur(cls, conn):
#         return conn.cursor()
#
#     @classmethod
#     def close_res(cls, conn, cur):
#         if cur:
#             cur.close()
#             cur = None
#         if conn:
#             conn.close()
#             conn = None
# user_email = 'simagousheng@itcast.cn'
# 1.找到字符串中@的位置
# 2.获得字符串中的子串
# 字符串切片

# user_email = 'simagousheng@itcast.cn'
# position = user_email.find('@')
# if position == -1:
#     print('@不存在，邮箱不合法！')
# else:
#     user_name = user_email[:position]
#     houu_zhui = user_email[position+1:]
#     print('用户名是：',user_name)
#     print('邮箱后缀：',houu_zhui)
# user_email = 'simagousheng@itcast.com'
# split 拆分 特别多
my_str = 'aa#b123#cc#dd'
ret = my_str.split('#')
print(ret)
print(ret[0])
print(ret[3])
user_email = 'simagousheng@itcast.com'
char_count = user_email.count('@')
if char_count > 1:
    print('你的邮箱不合法！')
else:
    result = user_email.split('@')
    print(user_email.split('@'))
    print('用户名：',result[0])
    print('邮箱后缀：',result[1])
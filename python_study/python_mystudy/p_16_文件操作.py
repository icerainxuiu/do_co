# 1.打开文件
file = open('readme')
# 2.读取文件内容
while True:
    text = file.readline()
    # 判断是否读取到内容
    if not text:
        break
    print(text)

# 3.关闭文件
file.close()
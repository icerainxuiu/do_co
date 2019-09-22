import os
"""
在当前文件夹创建1-10.txt文件，
并将其复制成副本1-10.txt
"""

for i in range(1, 11):
    f = open("%d.txt" % i, "w")
    f.close()


for j in range(1, 11):
    os.rename("./%d.txt" % j, "./副本%d.txt" % j)

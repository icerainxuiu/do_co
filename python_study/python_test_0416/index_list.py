import random


l1 = list()
# i = input("请输入你要删除的数1 -- 10")
n = 10
while n > 0:
    l1.append(random.randint(1, 10))
    n -= 1

# m = l1.count(i)
# if m != 0:
#     l1.remove(i)
print(l1,"\n", len(l1))
sun = 0
sun1 = 0
for i in l1:
    sun += i
print(sun)
for i in range(len(l1)):
    sun1 += l1[i]
print(sun)

# print(l1)
# l1.remove(58)
# print(l1)
# l1.extend(l2)
# print(l1)
# l1.pop()
# print(l1)
# l1.extend(l2)
# print(l1)
# l1.extend(l2)
# l1.extend(l2)
# print(l1)
# l1.pop(-3)
# print(l1)

dict1 = {"a": "a", "b": "b"}
dict2 = dict1.copy()
print(dict2)
print(id(dict1["a"]))
print(id(dict2["a"]))



# for i in l1:
#     l2.append(len(str(i)))
# l2.sort()
# print(l2[-1])
# n = 7
# while n > 0:
#     l1.append(input("输入字符"))
#     n -= 1
# char1 = input("输入你想查找的字符")
# start = int(input("输入你想查找的开始位置"))
# stop = int(input("输入你想查找的结束位置"))
# print("%s的index是%s" %(char1, l1.index(char1, start, stop)))
#
# for i in l1:
#     n = "" + i
# print(n.find("e"))


if __name__ == '__main__':
    n = 7

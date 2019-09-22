# from calculatea import calculatea
# # import calculatea
#
#
# calculatea.g_result = calculatea.div(1, 2)
# print(calculatea.g_result)
# calculatea.g_result = calculatea.mul(1, 23)
# print(calculatea.g_result)
# calculatea.g_result = calculatea.sub(1, 2)
# print(calculatea.g_result)
# calculatea.g_result = calculatea.add(1, 2)
# print(calculatea.g_result)
#
#






# list_val = list()
#
# try:
#     list_val[0] / 0
#     print(result)
# except (IndexError, ZeroDivisionError, NameError):
#     # print("Name Error")
#     list_val.append(1)
#     result = list_val[0] / 1
#     print(result)
    # try:
    #     print("Index Error")
    #     list_val.append(1)
    #     list_val[0] / 0
    # except ZeroDivisionError:
    #     try:
    #         print("除数不能为0")
    #         list_val[0] / 1
    #         print(result)
    #     except NameError:
    #         print("Name Error")
    #         result = list_val[0] / 1
    #         print(result)
# except ZeroDivisionError:
#     print("除数不能为0")
#     list_val[0]/1
# except NameError:
#     print("Name Error")
#     result = list_val[0]/1
#     print(result)

f = open("1.txt", "w")
while True:
    s = input("输入")
    if s == "exit":
        break
    s1 = s.upper()
    f.write(s1 + "\n")

f.close()
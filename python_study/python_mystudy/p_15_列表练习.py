# 1个学校有8个老师，3个办公室，请随机分配办公室
# 定义学校和办公室
school = [[],[],[]]
# 定义列表保存老师

import random

def create_teachers():
    """ 创建老师列表"""
    # 定义列表保存老师
    teacher_list = []
    index = 1
    while index <= 8:
        # 创建老师的名字
        teacher_name = '老师' + str(index)
        # 把老师装进笼子
        teacher_list.append(teacher_name)
        index += 1
    return teacher_list
# 分配老师
teachers_list = create_teachers()
print(teachers_list)

for teacher in teachers_list:
    # 产生一个办公室随机编号
    office_number = random.randint(0,2)
    # 给老师随机分配办公室
    school[office_number].append(teacher)
# 查看下各个办公室的老师
for office in school:
    for person in office:
        print(person,end=' ')
    print()
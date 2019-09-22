import random


def teachers_list():
    teacher_list = []
    for j in range(1, 10):
        teacher_name = "老师" + str(j)
        teacher_list.append(teacher_name)
    return teacher_list


school = [[], [], []]
for teacher in teachers_list():
    i = random.randint(0, 2)
    # print(i)
    school[i].append(teacher)
print(school)

for y in school:
    for x in y:
        print(x, end='\t')
    print()



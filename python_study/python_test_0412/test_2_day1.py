studentNo = input("请输入学生学号")
studentName = input("请输入学生姓名")
ChineseScore = input("请输入语文成绩")
MathScore = input("请输入数学成绩")
print(type(studentName))
print(type(studentNo))
print(type(ChineseScore))
print(type(MathScore))
ChineseScore = int(ChineseScore)
MathScore = int(MathScore)
list1 = [0]
list1.append(ChineseScore)
list1.append(MathScore)
sum1 = sum(list1)
print(sum1 / 2)
print(sum1)

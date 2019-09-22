# 根据分数显示档位
"""
1.获得输入的分数
2.拿到的数据是什么类型，将获得的数据转换为数字类型
3.根据分数分档
  3.1 90-100 A
  3.2 80-90 B
  3.3 70-80 C
  3.4 60-70 D
  3.5 60以下 E
"""
# 获得用户输入分数
score = float(input('请输入分数：'))
if score <=100 and score >= 0:
    if score >= 90 and score <= 100:
        print('您太棒了！')
    elif score >= 80 and score < 90:
        print('您很一般')
    elif score >= 70 and score < 80:
        print('您一般般了')
    elif score >= 60 and score < 70:
        print('及格')
    else:
        print('您完了！！！')
else:
    print('输入错误！')
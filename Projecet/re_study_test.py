# 2、Python中正则表达式模块re

# 前面区号+电话号码的例子

# （1）判断某个字符串是否匹配特定的模式

# 导入re模块
import re
#
# # 匹配
# print('x' * 20)
# result = re.match(r'\d{3,4}\-\d{3,8}', '020-12345')
# print(result)
# print('x' * 20)
#
# # 不匹配
# result2 = re.match(r'\d{3,4}\-\d{3,8}$', '020 12345')
# print(result2)
#
# # match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。
# # 常见的判断方法就是：
#
# # 带判断的字符串
#
# test = "020\n12345"
# print(test)
# if re.match(r'\d{3,4}\\n\d{3,8}', test):
#     print('match')
# else:
#     print('not match')
#
# # 小练习：判断给定的邮箱地址是否是NETEC邮箱
# # （1）假设NETEC公司的邮箱格式为姓+.+名字+数字+@netec.com.cn。
# # （2）其中数字不是必须的，只有相同名字的员工有多个时，才会存在数字
# # （3）并且姓名拼音或英文都会使用小写字母，而不会使用大写字母
#
# email = 'lee.jack3@netec.com.cn'
#
# pattern = r'^[a-z]{1,}\.[a-z]+\d*@netec.com.cn$'
#
# if re.match(pattern, email):
#     print('是NETEC邮箱')
# else:
#     print('不是NETEC邮箱')
#
# # （2）切分字符串
#
# # 用正则表达式切分字符串比用固定的字符更灵活，请看正常的切分代码：
# print('&' * 20)
# result3 = 'a b   c'.split(' ')
# print(result3)
#
# # 无法识别连续的空格，用正则表达式试试:
# result4 = re.split(r'\s+', 'a b   c')
# print(result4)
#
# # 无论多少个空格都可以正常分割。加入,试试：
#
# result5 = re.split(r'[\s\,]+', 'a,b,, c  d')
# print(result5)
#
# # 再加入;试试：
# result6 = re.split(r'[\s\,\;]+', 'a,b;; c  d')
# print(result6)
#
# # （3）提取特定模式的字符串
#
# # 除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。
# # 用()表示的就是要提取的分组（Group）。比如：^(\d{3,4})-(\d{3,8})$
# # 分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码：
#
# m = re.match(r'^(\d{3,4})-(\d{3,8}$)', '0755-12345')
# print(m)
# print(m.group(0))  # 匹配的整个字符串
# print(m.group(1))  # 匹配的第一个小括号的内容，即第一个匹配的子串
# print(m.group(2))  # 匹配的第二个小括号的内容，即第二个匹配的子串
#
#
# # （4）将指定模式的字符串进行替换
# print('&' * 20)
# result = re.sub('[ae]', 'X', 'abcdefghi')
# print(result)
#
# result = re.subn('[ae]', 'X', 'abcdef')
# print(result)
#
# # （5）贪婪匹配 vs 非贪婪匹配
#
# # 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。举例如下，匹配出数字后面的0：
# # \d+   '3243423'
# print('I' * 20)
# result7 = re.match(r'^(\d+)(0*)$', '102300').groups()  # group[1] group[2]
# print(result7)
#
# # 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
# # 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，
# # 加个?就可以让\d+采用非贪婪匹配：
#
# result8 = re.match(r'(\d+?)(0+?)(\d+)', '11002300000').groups()
# print(result8)
#
# # （6）正则表达式的编译
#
# # 当我们在Python中使用正则表达式时，re模块内部会干两件事情：
# #   1、编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
# #   2、用编译后的正则表达式去匹配字符串。
#
# # 如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，
# # 接下来重复使用时就不需要编译这个步骤了，直接匹配：
#
# # 编译
# re_telephone = re.compile(r'^(\d{3,4})-(\d{3,8})$')
#
# # 直接使用
# print(re_telephone.match('010-12345').groups())
#
# # 直接使用
# print(re_telephone.match('010-8086').groups())
#
# # 编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，
# # 所以调用对应的方法时不用给出正则字符串。
#
#
# # （7）re模块中常用的几个函数
#
# # compile() 编译正则表达式模式，返回一个对象的模式，这样某个模式编译一次就可以在程序中多次使用
#
#
# tt = "Tina is a good girl, she is cool, clever, and so on..."
# print(tt)
# rr = re.compile(r'\w*oo\w*')
# print(rr.findall(tt))  # 查找所有包含'oo'的单词
#
# # match() 决定RE是否在字符串刚开始的位置匹配。//注：这个方法并不是完全匹配。
# # 当pattern结束时若string还有剩余字符，仍然视为成功。想要完全匹配，可以在表达式末尾加上边界匹配符'$'
#
# print(re.match('com', 'comwww.runcomoob').group())
#
# # search() re.search函数会在字符串内查找模式匹配,只要找到第一个匹配然后返回，如果字符串没有匹配，则返回None。
#
# print(re.search(r'\dcom', 'www.4comrunoob.5com').group())
#
# # findall() 遍历匹配，可以获取字符串中所有匹配的字符串，返回一个列表。
#
# p = re.compile(r'\d+')
# print(p.findall('o1n2m3k4'))
#
# # finditer() 搜索string，返回一个顺序访问每一个匹配结果（Match对象）的迭代器。找到 RE 匹配的所有子串，并把它们作为一个迭代器返回。
#
# item = re.finditer(r'\d+', '12 drumm44ers drumming, 11 ... 10 ...')
# for i in item:
#     print(i)
#     print(i.group())
#     print(i.span())
#
# # split() 按照能够匹配的子串将string分割后返回列表。
# # 可以使用re.split来分割字符串，如：re.split(r'\s+', text)；将字符串按空格分割成一个单词列表。
# print(re.split(r'\d+', 'one1two2three3four4five5'))
#
# # sub() 使用re替换string中每一个匹配的子串后返回替换后的字符串。
#
#
# text = "JGood is a handsome boy, he is cool, clever, and so on..."
# print(re.sub(r'\s+', '-', text))
#
# # subn() 使用re替换string中每一个匹配的子串后返回替换后的字符串，并返回替换次数
#
# print(re.subn('[1-2]', 'A', '123456abcdef'))
# print(re.sub("g.t", "have", 'I get A,  I got B ,I gut C'))
# print(re.subn("g.t", "have", 'I get A,  I got B ,I gut C'))
#
# # 匹配IP
# result = re.search(
#     r"(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5]\.)",
#     "192.168.1.1")
# print(result)

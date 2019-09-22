# 引入线程和时间包
import threading
import time


# 创建一个道歉函数
def sorry():
        print("My dear, I'm sorry!")
        time.sleep(1)  # 休眠1秒


# 创建一个跳舞函数
def dance():
        print("Let me dancing with you")
        time.sleep(1)


def main():
    for i in range(5):
        t1 = threading.Thread(target=sorry)  # 创建线程对象 t1 和 t2
        t2 = threading.Thread(target=dance)  # 分别指向道歉和跳舞
        t1.start()  # 执行道歉线程
        t2.start()  # 执行跳舞线程
        time.sleep(1)


if __name__ == "__main__":
    main()
import os
import time
source = [r'C:\Users\icerain\Desktop']

target_dir = r'D:\ '
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
print(target)
zip_command = ('zip -qr %s %s' % (target, ' '.join(source)))
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup faild')
# 到目前为止 在我们的程序中，我们都是根据操作数据的函数或语句块来设计程序
# 者被称为面向过程的编程，还有一种把数据和功能结合起来
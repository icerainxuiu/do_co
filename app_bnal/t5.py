import random

import matplotlib
from matplotlib import pyplot as plt


font = {'family': "MicroSoft YaHei",
        "weight": "bold"
        }
matplotlib.rc("font", **font)


y = [1, 0, 1, 2, 1, 1, 2, 4, 3, 2, 4, 1, 4, 1, 3, 4, 5, 2, 1, 2]
x = range(11, 31)
y1 = [random.randint(0, 5) for i in range(20)]

plt.figure(figsize=(20, 8), dpi=80)
plt.plot(x, y, label="自己", color="orange")
plt.plot(x, y1, label="同桌", color="cyan")
plt.xlabel("年龄")

plt.ylabel("女朋友数")

_xtick_labels = ["{}岁".format(i) for i in x]

plt.xticks(x, _xtick_labels)
plt.title("11到30岁每年女朋友数量")

plt.grid(alpha=0.3)
plt.legend()
plt.show()



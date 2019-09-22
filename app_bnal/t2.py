
import random
import matplotlib
from matplotlib import pyplot as plt
fig = plt.figure(figsize=(20, 10), dpi=80)


font = {'family': "MicroSoft YaHei",
        "weight": "bold"
        }
matplotlib.rc("font", **font)


x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]
plt.plot(x, y)

_x = list(x)
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]
plt.xticks(list(x)[::3], _xtick_labels[::3], rotation=45)
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("10点到12点每分钟的温度变化")

plt.show()


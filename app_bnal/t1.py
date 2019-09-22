from matplotlib import pyplot as plt
fig = plt.figure(figsize=(20, 10), dpi=80)


x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]
plt.plot(x, y)

plt.xticks(x)
plt.yticks(y)


plt.show()

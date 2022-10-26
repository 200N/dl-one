import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1000,10)
y = np.linspace(0,500,10)
X,Y = np.meshgrid(x, y)#网格点

plt.plot(X, Y,
         color='green',  # 设置颜色为limegreen
         marker='x',  # 设置点类型为圆点
         linestyle='')  # 设置线型为空，也即没有线连接点
plt.grid(True)
plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0.05, 10, 1000)
# y = np.random.rand(1000)

# plt.scatter(x, y, label="scatter figure")

# plt.legend()

# plt.xlim(0.05, 10)
# plt.ylim(0, 1)

# plt.show()

import matplotlib.pyplot as plt  # 导入Matplotlib用于绘图
from mpl_toolkits.mplot3d import Axes3D  # 导入3D绘图工具
import numpy as np  # 导入NumPy用于生成随机数据

# 创建3D图表
fig = plt.figure()  # 创建新图表
ax = fig.add_subplot(111, projection='3d')  # 添加3D坐标轴

# 数据
x = np.random.rand(50)  # 随机生成X轴数据
y = np.random.rand(50)  # 随机生成Y轴数据
z = np.random.rand(50)  # 随机生成Z轴数据

# 配置字体
plt.rcParams['font.family'] = 'Times New Roman'

# 绘制3D散点图
ax.scatter(x, y, z, color='purple')  # 绘制紫色3D散点图
ax.set_xlabel('X Axis')  # 设置X轴标签
ax.set_ylabel('Y Axis')  # 设置Y轴标签
ax.set_zlabel('Z Axis')  # 设置Z轴标签
plt.title('3D Scatter Plot')  # 设置标题

plt.savefig("3d_scatter_plot.png", dpi=300, bbox_inches='tight')  # 将图片保存为高分辨率PNG格式

plt.show()  # 显示图表

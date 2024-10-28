import matplotlib.pyplot as plt  # 导入Matplotlib用于绘图
from mpl_toolkits.mplot3d import Axes3D  # 导入3D绘图工具
import numpy as np  # 导入NumPy用于生成数据

# 数据
x = np.arange(4)  # X轴上的4个条形
y = np.arange(3)  # Y轴上的3个条形
x, y = np.meshgrid(x, y)  # 创建网格
x = x.ravel()  # 扁平化数组
y = y.ravel()  # 扁平化数组
z = np.zeros_like(x)  # Z轴的起始点
dx = dy = 0.5  # 条形图的宽度
dz = np.random.rand(12)  # Z轴的高度，随机生成12个值

# 配置字体
plt.rcParams['font.family'] = 'Times New Roman'

# 绘制3D条形图
fig = plt.figure()  # 创建新图表
ax = fig.add_subplot(111, projection='3d')  # 添加3D子图
ax.bar3d(x, y, z, dx, dy, dz, color='skyblue')  # 绘制3D条形图
ax.set_title('3D Bar Plot')  # 设置标题
ax.set_xlabel('X-axis')  # 设置X轴标签
ax.set_ylabel('Y-axis')  # 设置Y轴标签
ax.set_zlabel('Z-axis')  # 设置Z轴标签
plt.savefig("3d_bar_plot.png", dpi=300, bbox_inches='tight')  # 将图片保存为高分辨率PNG格式

plt.show()  # 显示图表

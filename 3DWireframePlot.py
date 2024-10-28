import matplotlib.pyplot as plt  # 导入Matplotlib用于绘图
from mpl_toolkits.mplot3d import Axes3D  # 导入3D绘图工具
import numpy as np  # 导入NumPy用于生成数据

# 生成X, Y数据网格
x = np.linspace(-5, 5, 50)  # 在-5到5之间生成50个数据点
y = np.linspace(-5, 5, 50)  # 在-5到5之间生成50个数据点
X, Y = np.meshgrid(x, y)  # 创建网格
Z = np.sin(np.sqrt(X**2 + Y**2))  # 计算Z轴值

# 配置字体
plt.rcParams['font.family'] = 'Times New Roman'

# 绘制3D线框图
fig = plt.figure()  # 创建新图表
ax = fig.add_subplot(111, projection='3d')  # 添加3D子图
ax.plot_wireframe(X, Y, Z, color='brown')  # 绘制线框图
ax.set_title('3D Wireframe Plot')  # 设置标题
ax.set_xlabel('X-axis')  # 设置X轴标签
ax.set_ylabel('Y-axis')  # 设置Y轴标签
ax.set_zlabel('Z-axis')  # 设置Z轴标签
plt.savefig("3d_wireframe_plot.png", dpi=300, bbox_inches='tight')  # 将图片保存为高分辨率PNG格式

plt.show()  # 显示图表

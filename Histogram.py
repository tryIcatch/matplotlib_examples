import matplotlib.pyplot as plt  # 导入Matplotlib用于绘图
import numpy as np  # 导入NumPy用于生成数据

# 数据
data = np.random.normal(size=1000)  # 生成正态分布数据

# 配置字体
plt.rcParams['font.family'] = 'Times New Roman'

# 绘制直方图
plt.hist(data, bins=30, color='skyblue', edgecolor='black')  # 绘制蓝色直方图，30个柱子，黑色边框
plt.title('Histogram')  # 设置标题
plt.xlabel('Value')  # 设置X轴标签
plt.ylabel('Frequency')  # 设置Y轴标签
plt.savefig("histogram.png", dpi=300,bbox_inches='tight', transparent=True)  # 分辨率300 DPI，适合高清打印

plt.show()  # 显示图表

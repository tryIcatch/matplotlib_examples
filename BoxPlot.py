import matplotlib.pyplot as plt  # 导入Matplotlib用于绘图
import numpy as np  # 导入NumPy用于生成数据

# 生成数据
data = np.random.normal(size=100)  # 生成正态分布的数据样本

# 配置字体
plt.rcParams['font.family'] = 'Times New Roman'

# 绘制箱线图
plt.boxplot(data)  # 绘制箱线图
plt.title('Box Plot')  # 设置标题

plt.savefig("box_chart.png", dpi=300,bbox_inches='tight', transparent=True)  # 分辨率300 DPI，适合高清打印

plt.show()  # 显示图表

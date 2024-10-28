import matplotlib.pyplot as plt  # 导入Matplotlib用于绘图
import numpy as np  # 导入NumPy用于计算累计百分比

# 数据
categories = ['A', 'B', 'C', 'D', 'E']  # 分类标签
values = [10, 20, 15, 25, 30]  # 每个分类的值
cumulative_percentage = np.cumsum(values) / sum(values) * 100  # 计算累计百分比

# 配置字体
plt.rcParams['font.family'] = 'Times New Roman'

# 绘制帕累托图
fig, ax1 = plt.subplots()  # 创建图表及第一个坐标轴
ax1.bar(categories, values, color='skyblue')  # 绘制柱状图，显示分类数据
ax1.set_xlabel('Categories')  # 设置X轴标签
ax1.set_ylabel('Values', color='skyblue')  # 设置左Y轴标签和颜色

ax2 = ax1.twinx()  # 创建双坐标轴
ax2.plot(categories, cumulative_percentage, color='orange', marker='D', linestyle='-')  # 绘制折线图显示累计百分比
ax2.set_ylabel('Cumulative Percentage (%)', color='orange')  # 设置右Y轴标签和颜色
plt.title('Pareto Chart')  # 设置标题

plt.savefig("pare2chart.png", dpi=300,bbox_inches='tight', transparent=True)  # 分辨率300 DPI，适合高清打印

plt.show()  # 显示图表

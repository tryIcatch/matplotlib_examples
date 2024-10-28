import matplotlib.pyplot as plt  # 导入Matplotlib用于绘图

# 数据
x = [1, 2, 3, 4, 5]  # X轴数据
y = [10, 14, 15, 18, 20]  # Y轴数据

# 配置字体为Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'

# 绘制散点图
plt.scatter(x, y, color='blue', marker='o')  # 生成散点图，蓝色圆形标记
plt.title('Scatter Plot')  # 设置图表标题
plt.xlabel('X-axis')  # 设置X轴标签
plt.ylabel('Y-axis')  # 设置Y轴标签
plt.savefig("scatter_plot.png", dpi=300,bbox_inches='tight', transparent=True)  # 分辨率300 DPI，适合高清打印

plt.show()  # 显示图表

import matplotlib.pyplot as plt  # 导入Matplotlib用于绘图

# 数据
x = [1, 2, 3, 4, 5]  # X轴数据
y = [2, 4, 6, 8, 10]  # Y轴数据

# 配置字体
plt.rcParams['font.family'] = 'Times New Roman'

# 绘制折线图
plt.plot(x, y, color='green', marker='o')  # 生成绿色折线图，带圆形标记
plt.title('Line Chart')  # 设置标题
plt.xlabel('X-axis')  # 设置X轴标签
plt.ylabel('Y-axis')  # 设置Y轴标签
plt.savefig("line_chart.png", dpi=300,bbox_inches='tight', transparent=True)  # 分辨率300 DPI，适合高清打印

plt.show()  # 显示图表

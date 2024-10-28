import matplotlib.pyplot as plt  # 导入Matplotlib用于绘图

# 数据
categories = ['A', 'B', 'C', 'D']  # 分类标签
values = [5, 7, 8, 6]  # 每个分类的数值

# 配置字体
plt.rcParams['font.family'] = 'Times New Roman'

# 绘制柱状图
plt.bar(categories, values, color='orange')  # 生成橙色柱状图
plt.title('Bar Chart')  # 设置标题
plt.xlabel('Categories')  # 设置X轴标签
plt.ylabel('Values')  # 设置Y轴标签
plt.savefig("bar_chart.png", dpi=300,bbox_inches='tight', transparent=True)  # 分辨率300 DPI，适合高清打印

plt.show()  # 显示图表

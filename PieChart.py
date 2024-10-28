import matplotlib.pyplot as plt  # 导入Matplotlib用于绘图

# 数据
labels = ['Apple', 'Banana', 'Cherry', 'Date']  # 分类标签
sizes = [15, 30, 45, 10]  # 每个分类的占比

# 配置字体
plt.rcParams['font.family'] = 'Times New Roman'

# 绘制饼图
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)  # 绘制饼图，显示百分比，起始角度140度
plt.title('Pie Chart')  # 设置标题
plt.savefig("pie_chart.png", dpi=300,bbox_inches='tight', transparent=True)  # 分辨率300 DPI，适合高清打印

plt.show()  # 显示图表

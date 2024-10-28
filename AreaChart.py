import matplotlib.pyplot as plt  # 导入Matplotlib用于绘图

# 数据
x = [1, 2, 3, 4, 5]  # X轴数据
y1 = [1, 4, 6, 8, 9]  # Y轴下方区域的数据
y2 = [2, 2, 7, 10, 12]  # Y轴上方区域的数据

# 配置字体
plt.rcParams['font.family'] = 'Times New Roman'

# 绘制面积图
plt.fill_between(x, y1, color="skyblue", alpha=0.4)  # 绘制y1的面积图，颜色为天蓝色，透明度0.4
plt.fill_between(x, y2, color="orange", alpha=0.4)  # 绘制y2的面积图，颜色为橙色，透明度0.4
plt.title('Area Chart')  # 设置标题
plt.xlabel('X-axis')  # 设置X轴标签
plt.ylabel('Y-axis')  # 设置Y轴标签

# 保存图片，设置分辨率为300 DPI
plt.savefig("area_chart.png", dpi=300,bbox_inches='tight', transparent=True)  # 分辨率300 DPI，适合高清打印

plt.show()  # 显示图表

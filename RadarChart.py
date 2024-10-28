import matplotlib.pyplot as plt  # 导入Matplotlib用于绘图
import numpy as np  # 导入NumPy用于生成数据

# 数据
labels = ['A', 'B', 'C', 'D', 'E']  # 数据标签
values = [4, 3, 5, 2, 4]  # 各标签的值

angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()  # 计算角度
values += values[:1]  # 闭合多边形
angles += angles[:1]  # 闭合多边形

# 配置字体
plt.rcParams['font.family'] = 'Times New Roman'

# 绘制雷达图
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))  # 创建极坐标轴
ax.fill(angles, values, color='purple', alpha=0.25)  # 填充多边形，设置透明度
ax.plot(angles, values, color='purple', linewidth=2)  # 绘制紫色多边形
ax.set_yticklabels([])  # 隐藏极轴刻度标签
ax.set_xticks(angles[:-1])  # 设置X轴标签
ax.set_xticklabels(labels)  # 添加标签
plt.title('Radar Chart')  # 设置标题
plt.savefig("rader_chart.png", dpi=300,bbox_inches='tight', transparent=True)  # 分辨率300 DPI，适合高清打印

plt.show()  # 显示图表

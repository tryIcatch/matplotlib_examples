import matplotlib.pyplot as plt  # 导入Matplotlib用于绘图
import numpy as np  # 导入NumPy用于计算角度

# 数据
labels = ['Speed', 'Reliability', 'Comfort', 'Safety', 'Efficiency']  # 数据标签
values = [3, 4, 5, 2, 4]  # 各项指标的值
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()  # 计算每个点的角度
values += values[:1]  # 闭合图形环绕
angles += angles[:1]  # 闭合图形环绕

# 配置字体
plt.rcParams['font.family'] = 'Times New Roman'

# 绘制蜘蛛网图
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))  # 创建极坐标轴
ax.fill(angles, values, color='red', alpha=0.25)  # 填充区域，设置颜色和透明度
ax.plot(angles, values, color='red', linewidth=2)  # 绘制线条
ax.set_yticklabels([])  # 隐藏极轴标签
ax.set_xticks(angles[:-1])  # 设置X轴标签
ax.set_xticklabels(labels)  # 添加标签
plt.title('Spider Chart')  # 设置标题
plt.savefig("spider_chart.png", dpi=300,bbox_inches='tight', transparent=True)  # 分辨率300 DPI，适合高清打印

plt.show()  # 显示图表

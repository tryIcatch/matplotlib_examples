import matplotlib.pyplot as plt  # 导入Matplotlib用于绘图
import numpy as np  # 导入NumPy用于生成数据

# 数据
angles = np.linspace(0, 2 * np.pi, 8, endpoint=False).tolist()  # 生成8个角度，分布在0到2π
angles += angles[:1]  # 封闭多边形环绕

values = [1, 2, 3, 4, 5, 6, 7, 1]  # 数据点，形成多边形图形
values += values[:1]  # 封闭多边形环绕

# 配置字体
plt.rcParams['font.family'] = 'Times New Roman'

# 绘制极坐标图
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))  # 创建极坐标轴
ax.plot(angles, values, color='blue', linewidth=2, linestyle='solid')  # 绘制蓝色实线图形
ax.fill(angles, values, color='blue', alpha=0.25)  # 填充图形，设置透明度
plt.title('Polar Chart')  # 设置标题
plt.savefig("polar_chart.png", dpi=300,bbox_inches='tight', transparent=True)  # 分辨率300 DPI，适合高清打印

plt.show()  # 显示图表

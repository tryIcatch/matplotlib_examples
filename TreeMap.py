import squarify  # 导入Squarify库用于生成树状图
import matplotlib.pyplot as plt  # 导入Matplotlib用于绘图

# 数据
values = [500, 300, 100, 200, 700]  # 各分类的大小
labels = ['A', 'B', 'C', 'D', 'E']  # 分类标签
colors = ['skyblue', 'orange', 'purple', 'green', 'red']  # 设置每块的颜色

# 配置字体
plt.rcParams['font.family'] = 'Times New Roman'

# 绘制树状图
squarify.plot(sizes=values, label=labels, color=colors, alpha=0.7)  # 绘制树状图，带标签，设置透明度
plt.axis('off')  # 隐藏坐标轴
plt.title('Tree Map')  # 设置标题
plt.savefig("tree_map.png", dpi=300,bbox_inches='tight', transparent=True)  # 分辨率300 DPI，适合高清打印

plt.show()  # 显示图表

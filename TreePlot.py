import matplotlib.pyplot as plt  # 导入Matplotlib用于绘图
import networkx as nx  # 导入NetworkX用于生成树形结构

# 创建树图
G = nx.balanced_tree(r=2, h=3)  # 创建一个二叉树，3层

# 配置字体
plt.rcParams['font.family'] = 'Times New Roman'

# 绘制树结构图
plt.figure(figsize=(8, 8))  # 设置图表大小
nx.draw(G, with_labels=True, node_color='skyblue', node_size=800, font_size=10)  # 绘制树图
plt.title('Tree Structure')  # 设置标题
plt.savefig("time_structure.png", dpi=300,bbox_inches='tight', transparent=True)  # 分辨率300 DPI，适合高清打印

plt.show()  # 显示图表

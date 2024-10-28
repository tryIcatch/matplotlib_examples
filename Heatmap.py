import seaborn as sns  # 导入Seaborn库用于高级数据可视化
import numpy as np  # 导入NumPy用于生成数据
import matplotlib.pyplot as plt  # 导入Matplotlib用于绘图

# 生成随机数据
data = np.random.rand(10, 10)  # 生成10x10随机矩阵

# 配置字体
plt.rcParams['font.family'] = 'Times New Roman'

# 绘制热力图
sns.heatmap(data, annot=True, cmap='coolwarm')  # 绘制热力图，带注释，颜色为冷暖色调
plt.title('Heatmap')  # 设置标题
plt.savefig("heata_map.png", dpi=300,bbox_inches='tight', transparent=True)  # 分辨率300 DPI，适合高清打印

plt.show()  # 显示图表

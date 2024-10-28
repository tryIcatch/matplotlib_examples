import seaborn as sns  # 导入Seaborn库用于高级数据可视化
import numpy as np  # 导入NumPy用于生成数据
import matplotlib.pyplot as plt  # 导入Matplotlib用于绘图

# 数据
data = np.random.normal(size=1000)  # 生成正态分布的随机数据

# 配置字体
plt.rcParams['font.family'] = 'Times New Roman'

# 绘制核密度图
sns.kdeplot(data, shade=True, color="purple")  # 绘制紫色核密度图，填充区域
plt.title('Kernel Density Estimation Plot')  # 设置标题
plt.savefig("kernel_density_estimation_plot.png", dpi=300,bbox_inches='tight', transparent=True)  # 分辨率300 DPI，适合高清打印

plt.show()  # 显示图表

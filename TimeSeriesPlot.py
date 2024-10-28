import matplotlib.pyplot as plt  # 导入Matplotlib用于绘图
import pandas as pd  # 导入Pandas用于生成时间序列数据

# 生成时间序列数据
dates = pd.date_range(start='2023-01-01', periods=30)  # 生成30天的日期范围
values = pd.Series(range(30), index=dates)  # 创建时间序列数据

# 配置字体
plt.rcParams['font.family'] = 'Times New Roman'

# 绘制时间序列图
values.plot(title="Time Series Plot", color="green", marker='o')  # 绘制折线图，带绿色圆形标记
plt.xlabel('Date')  # 设置X轴标签
plt.ylabel('Value')  # 设置Y轴标签
plt.savefig("time_series_plot.png", dpi=300,bbox_inches='tight', transparent=True)  # 分辨率300 DPI，适合高清打印

plt.show()  # 显示图表

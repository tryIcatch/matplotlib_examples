import matplotlib.pyplot as plt  # 导入Matplotlib用于绘图
import waterfall_chart  # 导入waterfall_chart库生成瀑布图

# 数据
data = ['Start', 'Income', 'Expenses', 'Investments', 'End']  # 数据标签
values = [100, 30, -20, 40, 150]  # 每个阶段的值

# 配置字体
plt.rcParams['font.family'] = 'Times New Roman'

# 绘制瀑布图
waterfall_chart.plot(data, values, Title="Waterfall Chart")  # 绘制瀑布图
plt.savefig("waterfall_chart.png", dpi=300,bbox_inches='tight', transparent=True)  # 分辨率300 DPI，适合高清打印

plt.show()  # 显示图表

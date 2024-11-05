import numpy as np
import matplotlib.pyplot as plt

# 神經元編號和位置
neuron_ids = np.arange(160.5,205,4)
center_neuron = 182.5  # 中心神經元位置
sigma = 3  # 控制分布的寬度（越大越平滑）

# 計算每個神經元的活性，使用高斯分布
activity_levels = np.exp(-0.5 * ((neuron_ids - center_neuron) ** 2) / (sigma ** 2))

def double_peak(x, center1=4, center2=12, sigma=1.5, amplitude1=1, amplitude2=1):
    # 計算每個高斯峰
    peak1 = amplitude1 * np.exp(-0.5 * ((x - center1) ** 2) / ((sigma ** 2)*3))
    peak2 = amplitude2 * np.exp(-0.5 * ((x - center2) ** 2) / ((sigma ** 2)*3))
    # 合併兩個峰
    return peak1 + peak2

# 定義範圍和參數
x_values = []
for i in range(16):
	x_values.append(3*i+160)
x_values = np.array(x_values)
center1 = 182.5-12   # 第一個高斯峰的中心
center2 = 182.5+12  # 第二個高斯峰的中心
sigma = 1.5   # 控制每個峰的寬度
amplitude1 = 1  # 第一個峰的高度
amplitude2 = 1  # 第二個峰的高度

# 計算雙峰函數的值
y_values = double_peak(x_values, center1, center2, sigma, amplitude1, amplitude2)
# 可視化活性分佈


plt.figure(figsize=(10, 5))
plt.plot(x_values, y_values, marker='o')
plt.title(f"Neuron Activity Distribution around Neuron {center_neuron}")
plt.xlabel("Neuron ID")
plt.ylabel("Activity Level")
plt.axvline(182.5, color = 'black', linestyle = 'dashed')
plt.xticks(np.arange(160, 207, 3))
plt.savefig("head.png")

plt.figure(figsize=(10, 5))
plt.plot(neuron_ids, activity_levels, marker='o')
plt.title(f"Neuron Activity Distribution around Neuron {center_neuron}")
plt.xlabel("Neuron ID")
plt.ylabel("Activity Level")
plt.axvline(182.5, color = 'black', linestyle = 'dashed')
plt.xticks(np.arange(160, 207, 3))
plt.savefig("goal.png")

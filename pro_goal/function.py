import iqif
import matplotlib.pyplot as plt
import json
import numpy as np

def neuron(potential):
	lines = []
	for filename in potential:
		with open(filename,'r') as f:
			for line in f:
				lines.append(int(line.strip(), 10))
	return lines

def update(list, tmp):
	# index = 5最舊  index = 0 最新
	for i in range(len(tmp)):
		for j in range(9,-1,-1):
			list[i][j] = list[i][j-1]
		list[i][0] = tmp[i]
	return list
    
# 讀取 JSON 檔案中的數據
def read_data_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data
    
def activity_levels(neuron_ids, center_neuron):
	sigma = 7  # 控制分布的寬度（越大越平滑）
	return np.exp(-0.5 * ((neuron_ids - center_neuron) ** 2) / (sigma ** 2))
	
def double_peak(x, center1=4, center2=12, sigma=3, amplitude1=1, amplitude2=1):
    # 計算每個高斯峰
    peak1 = amplitude1 * np.exp(-0.5 * ((x - center1) ** 2) / ((sigma ** 2)*3))
    peak2 = amplitude2 * np.exp(-0.5 * ((x - center2) ** 2) / ((sigma ** 2)*3))
    # 合併兩個峰
    return peak1 + peak2
    
def plot_activity(tmp_L, tmp_R):
	plt.figure()
	plt.plot(tmp_L, label='L')
	plt.plot(tmp_R, label='R')
	plt.plot([a + b for a, b in zip(tmp_L, tmp_R)], label='all')
	plt.legend()
	plt.xlabel('Time Step')
	plt.ylabel('Activity Level')
	plt.title('Neuron Activity Levels Over Time')
	plt.savefig('figure/LR.png')
	plt.close()
	
def plot_place(tmp_L, tmp_R, place):
	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx()
	ax1.plot([10*i for i in range(len(tmp_L))], tmp_L, color = 'blue', label = 'DN_L')
	ax1.plot([10*i for i in range(len(tmp_R))], tmp_R, color = 'red', label = 'DN_R')
	ax2.plot(place, color = 'green', label = 'place')
	ax2.set_ylim(0,48)
	ax2.axhline(24, color = 'black', linestyle = 'dashed')
	ax1.set_xlabel('time')
	ax1.set_ylabel('firing rate')
	ax2.set_ylabel('place')
	fig.legend(bbox_to_anchor = (0.9,0.3))
	fig.tight_layout()
	fig.savefig(f'figure/firingrate_place.png')
	
def plot_bar_chart(x, height, filename, xlabel, ylabel, color):
    plt.figure()
    plt.bar(x, height, color=color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(filename)
    plt.close()
    
def close_files(file_dict):
    for f in file_dict.values():
        f.close()


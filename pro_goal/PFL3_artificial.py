import iqif
import glob
import numpy as np
import math
import matplotlib.pyplot as plt
import time
from function import *
import sys

plot = True


net = iqif.lifnet("parameter/neuronParameter_LIF.txt", "parameter/Connection_Table_LIF.txt")
inhead_list = [f"inhead_{inhead}" for inhead in range(8)]
ingoal_list = [f"ingoal_{ingoal}" for ingoal in range(12)]
inheadin_list = ["inheadin_0"]
ingoalin_list = ["ingoalin_0"]
FC2_list = [f"FC2_{FC2}" for FC2 in range(12)]
headinput_list = [f"headinput_{headinput}" for headinput in range(16)]
PFL3_list = [f"PFL3_{PFL3}" for PFL3 in range(24)]
LAL_list = ['L', 'R', 'EL', 'ER', 'IL', 'IR', 'DN_L', 'DN_R']
neu_list = inhead_list+ingoal_list+inheadin_list+ingoalin_list+FC2_list+headinput_list+PFL3_list+LAL_list
potential = {n: open(f"potential/potential_{n}.txt", "w") for n in neu_list}
firingrate = {n: open(f"firingrate/firingrate_{n}.txt", "w") for n in neu_list}
FR_list = [[0 for j in range(10)] for i in range(len(neu_list))]
tmp_FR = [0 for i in range(len(neu_list))]

def activity_levels(neuron_ids, center):
	sigma = 7  # 控制分布的寬度（越大越平滑）
	return np.exp(-0.5 * ((neuron_ids - center) ** 2) / (sigma ** 2))

def double_peak(x, center1=4, center2=12, sigma=3, amplitude1=1, amplitude2=1):
    # 計算每個高斯峰
    peak1 = amplitude1 * np.exp(-0.5 * ((x - center1) ** 2) / ((sigma ** 2)*3))
    peak2 = amplitude2 * np.exp(-0.5 * ((x - center2) ** 2) / ((sigma ** 2)*3))
    # 合併兩個峰
    return peak1 + peak2
    
#parameter---------------------------------------------------------------------
pre_time = 2000
time = 18000
factor = 18
goallist = []
PFL3L_list = []
PFL3R_list = []

head = 24
goal = 0
for j in range(48):
	for time in range(200):
		for i in range(12):
			net.set_biascurrent(22+i, 17*activity_levels(i*4+2, goal))
		for i in range(16):
			net.set_biascurrent(34+i, 17*double_peak(i*3+1.5, center1 = head-12, center2 = head+12))
		net.send_synapse()
		

		for idx, n in enumerate(neu_list):
			potential[n].write(f"{int(net.potential(idx))}\n")
		if((time+1)%10==0):
			for idx, n in enumerate(neu_list):
				tmp_FR[idx] = net.spike_count(idx)
			FR_list = update(FR_list,tmp_FR)
			for idx, n in enumerate(neu_list):
				firingrate[n].write(f"{sum(FR_list[idx])}\n")
	goal+=1


for f in potential.values():
    f.close()
for f in firingrate.values():
    f.close()

if plot:
#--------------------PFL3----------------------------------------
	PFL3_L = []
	PFL3_R = []
	print("len = ", len(neuron(glob.glob(f"firingrate/firingrate_PFL3_0.txt"))))
	time = -10
	goal = 12
	for j in range(48):
		time+=20
		plt.figure()
		tmp_a = 0
		tmp_b = 0
		for i in range(12):
			a = neuron(glob.glob(f"firingrate/firingrate_PFL3_{2*i}.txt"))[time]
			b = neuron(glob.glob(f"firingrate/firingrate_PFL3_{2*i+1}.txt"))[time]
			plt.bar(2*i,a,color='red')
			plt.bar(2*i+1,b,color='blue')
			tmp_a += a
			tmp_b += b
		PFL3_L.append(tmp_a)
		PFL3_R.append(tmp_b)

		plt.xlabel('neuron index')
		plt.ylabel('r')
		plt.savefig(f'figure/PFL3_at_{goal}.png')
		plt.close()
		
		plt.figure()
		labels = []
		place = 2
		for i in range(12):
			plt.bar(i,neuron(glob.glob(f"firingrate/firingrate_FC2_{i}.txt"))[time],color='red')
			labels.append(place)
			place+=4
		plt.xticks(np.arange(12), labels, rotation=45)  # rotation=45
		plt.axvline(5.5, color = 'black', linestyle = 'dashed')
		plt.xlabel('neuron index')
		plt.ylabel('r')
		plt.savefig(f'figure/FC2_at_{goal}.png')
		plt.close()
		
		plt.figure()
		labels = []
		place = 1.5
		for i in range(16):
			plt.bar(i,neuron(glob.glob(f"firingrate/firingrate_headinput_{i}.txt"))[time],color='red')
			labels.append(place)
			place+=3
		plt.xticks(np.arange(16), labels, rotation=45)  # rotation=45
		plt.axvline(7.5, color = 'black', linestyle = 'dashed')
		plt.xlabel('neuron index')
		plt.ylabel('r')
		plt.savefig(f'figure/headinput_at_{goal}.png')
		plt.close()
		goal+=0.5
		
#--------------------------------------------------------------------------------------	
	plt.figure()
	tmp_x = []
	a = 12
	for i in range(48):
		tmp_x.append(a)
		a+=0.5
	plt.plot(tmp_x, PFL3_L, label = 'PFL3_L')
	plt.plot(tmp_x, PFL3_R, label = 'PFL3_R')
	tmp = []
	for i in range(len(PFL3_L)):
		tmp.append(PFL3_L[i]+PFL3_R[i])
	plt.plot(tmp_x, tmp, label = 'PFL3_L+R')
	plt.axvline((len(PFL3_L)/2)+0.5, color = 'black', linestyle = 'dashed')
	plt.legend()
	plt.savefig('figure/PFL3_LR.png')
	plt.close()


fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
#ax3 = ax1.twinx()
tmp = neuron(glob.glob("firingrate/firingrate_DN_L.txt"))
ax1.plot([10*i for i in range(len(tmp))], tmp, color = 'blue', label = 'DN_L')
tmp = neuron(glob.glob("firingrate/firingrate_DN_R.txt"))
ax1.plot([10*i for i in range(len(tmp))], tmp, color = 'red', label = 'DN_R')
ax2.plot(goallist, color = 'green', label = 'place')
ax2.set_ylim(0,48)
#ax3.plot([100*i for i in range(len(I_R))], I_R, label = 'I_R')
#ax3.plot([100*i for i in range(len(I_L))], I_L, label = 'I_L')
ax2.axhline(24, color = 'black', linestyle = 'dashed')
ax1.set_xlabel('time')
ax1.set_ylabel('firing rate')
ax2.set_ylabel('place')
fig.legend(bbox_to_anchor = (0.9,0.3))
fig.tight_layout()
fig.savefig(f'figure/firingrate_place.png')


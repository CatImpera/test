import iqif
import glob
import numpy as np
import math
import matplotlib.pyplot as plt
import time
import json
from function import *
import sys

#data & list-------------------------------------------------------------------
net = iqif.lifnet("parameter/neuronParameter_LIF.txt", "parameter/Connection_Table_LIF.txt")
data = read_data_from_json("parameter/neu_list.json")
neu_list = data['neu_list']
potential = {n: open(f"potential/potential_{n}.txt", "w") for n in neu_list}
firingrate = {n: open(f"firingrate/firingrate_{n}.txt", "w") for n in neu_list}
FR_list = [[0 for j in range(10)] for i in range(len(neu_list))]
tmp_FR = [0 for i in range(len(neu_list))]
goallist = []
    
#parameter---------------------------------------------------------------------
pre_time = 2000
time = 10000   # run in 2000~10000 ms
factor = 18
fold = 0.004

############
head = 24  #
goal = 14  #
############

for t in range(time):
	left_motor = sum(FR_list[80])
	right_motor = sum(FR_list[81])
	turn = (left_motor-right_motor)*fold
	if t>pre_time:
		goal = goal + turn
	goallist.append(goal)

	for i in range(12):
		net.set_biascurrent(22+i, 15*activity_levels(i*4+2, goal))
	for i in range(16):
			net.set_biascurrent(34+i, 17*double_peak(i*3+1.5, center1 = head-12, center2 = head+12))
	
	if (t>4500 and t<5000):
		net.set_biascurrent(86, 15)
		net.set_biascurrent(87, 14)
	else:
		net.set_biascurrent(86, 0)
		net.set_biascurrent(87, 0)
	net.send_synapse()

	for idx, n in enumerate(neu_list):
		potential[n].write(f"{int(net.potential(idx))}\n")
	if((t+1)%10==0):
		for idx, n in enumerate(neu_list):
			tmp_FR[idx] = net.spike_count(idx)
		FR_list = update(FR_list,tmp_FR)
		for idx, n in enumerate(neu_list):
			firingrate[n].write(f"{sum(FR_list[idx])}\n")

close_files(potential)
close_files(firingrate)

#----------------------------------------------------------
tmp_L = []
tmp_R = []
tmp_all = []

for j in range(0,time,500):
    tmp_a = sum(neuron(glob.glob(f"firingrate/firingrate_PFL3_{2 * i}.txt"))[int(j / 10)] for i in range(12))
    tmp_b = sum(neuron(glob.glob(f"firingrate/firingrate_PFL3_{2 * i + 1}.txt"))[int(j / 10)] for i in range(12))
    tmp_L.append(tmp_a)
    tmp_R.append(tmp_b)
    tmp_all.append(tmp_a + tmp_b)
	
"""
    # Plot PFL3 activity
    colors = ['red' if i % 2 == 0 else 'blue' for i in range(24)]
    plot_bar_chart(range(24), [neuron(glob.glob(f"firingrate/firingrate_PFL3_{i}.txt"))[int(j / 10)] for i in range(24)],
                   f'figure/PFL3_at_t{j}.png', 'neuron index', 'r', colors)
	
    # Plot headinput activity
    plot_bar_chart(range(16), [neuron(glob.glob(f"firingrate/firingrate_headinput_{i}.txt"))[int(j / 10)] for i in range(16)],
                       f'figure/headinput_at_{j}.png', 'neuron index', 'r', 'red')
                       
    # Plot FC2 activity                  
    plot_bar_chart(range(12), [neuron(glob.glob(f"firingrate/firingrate_FC2_{i}.txt"))[int(j / 10)] for i in range(12)],
                       f'figure/FC2_at_{j}.png', 'neuron index', 'r', 'red')
"""
plot_activity(tmp_L, tmp_R)
plot_place(neuron(glob.glob("firingrate/firingrate_DN_L.txt")),
			neuron(glob.glob("firingrate/firingrate_DN_R.txt")), goallist)



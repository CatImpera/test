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
def place_trace(goal_input):
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
	goal = goal_input  #
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
	return goallist
	
plt.figure()
for i in range(12,24,2):
	plt.plot(place_trace(i),label = f'i')
plt.legend()
plt.savefig("figure/place_trace.png")
plt.close()

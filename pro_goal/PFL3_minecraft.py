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
headlist = []
strength_list = []
time_list = []
#parameter---------------------------------------------------------------------
sim_time = 10000   
factor = 18
fold = 0.5
strength = 0
t0 = time.time()

############
head = 171  #
goal = 182.5  #
############

for t in range(sim_time):

	for i in range(12):
		net.set_biascurrent(22+i, 15*activity_levels(160.5+4*i, goal))
	for i in range(16):
			net.set_biascurrent(34+i, 17*double_peak(160+3*i, center1 = head-12, center2 = head+12))
	net.send_synapse()

	for idx, n in enumerate(neu_list):
		potential[n].write(f"{int(net.potential(idx))}\n")
	if((t+1)%10==0):
		for idx, n in enumerate(neu_list):
			tmp_FR[idx] = net.spike_count(idx)
		FR_list = update(FR_list,tmp_FR)
		for idx, n in enumerate(neu_list):
			firingrate[n].write(f"{sum(FR_list[idx])}\n")
	if((t+1)%100==0):
		#print('1 loop:',time.time()-t_start)
		t_start = time.time()
		left_motor = sum(FR_list[80])  #DN_L firingrate
		right_motor = sum(FR_list[81]) #DN_R firingrate
		turn = (right_motor-left_motor)*fold
		strength = int(2*abs(turn))
		print("loop    place         turn          strength    direction")
		print("{:<6} {:>10} {:>8} {:>10}           ".format(t, head, turn, strength), end = '')
		try:
			with open('/home/tim/.var/app/org.prismlauncher.PrismLauncher/data/PrismLauncher/instances/1.12.2_pipe_input_lua_240514/.minecraft/mods/advancedMacros/macros/turn', 'w') as f:

				if (strength == 0):
					print("o")
				elif turn>0:
					print("->",strength)
					#print("tmp = ","Right "+str(strength))
					f.write("R"+str(strength))
				elif turn<0:
					print("<-",strength)
					f.write("L"+str(strength))
		except:
			print('pass')
			pass
		try:
			with open('/home/tim/.var/app/org.prismlauncher.PrismLauncher/data/PrismLauncher/instances/1.12.2_pipe_input_lua_240514/.minecraft/mods/advancedMacros/macros/pose', 'r') as pose:
				line = pose.readline()
				if line:
					t, tx, ty, tz, rx, ry = line.strip().split()
					t, tx, ty, tz, rx, ry = map(float, [t, tx, ty, tz, rx, ry])
					head = tz
		except Exception as e:
			print('fail', e)
		#print('head = ', head)
		headlist.append(head)
		strength_list.append(strength)
		time_list.append(time.time()-t0)
	time.sleep(0.001)
	
close_files(potential)
close_files(firingrate)

#----------------------------------------------------------
plot_place(neuron(glob.glob("firingrate/firingrate_DN_L.txt")),
			neuron(glob.glob("firingrate/firingrate_DN_R.txt")), headlist)



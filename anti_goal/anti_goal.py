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
fold = 0.002
############
head = 24  #
goal = 30  #
############

for t in range(time):

	left_motor = sum(FR_list[6])
	right_motor = sum(FR_list[7])
	turn = (left_motor-right_motor)*fold
	if t>pre_time:
		goal = goal + turn
	goallist.append(goal)
	
	net.set_biascurrent(4, 11)
	net.set_biascurrent(5, 15)
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
fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8)) = plt.subplots(2, 4, sharex=True, sharey=False)
fig.suptitle('firing rate')
ax1.plot(neuron(glob.glob("firingrate/firingrate_L017.txt")))
ax5.plot(neuron(glob.glob("firingrate/firingrate_R017.txt")))
ax2.plot(neuron(glob.glob("firingrate/firingrate_L112.txt")))
ax6.plot(neuron(glob.glob("firingrate/firingrate_R112.txt")))
ax3.plot(neuron(glob.glob("firingrate/firingrate_L153.txt")))
ax7.plot(neuron(glob.glob("firingrate/firingrate_R153.txt")))
ax4.plot(neuron(glob.glob("firingrate/firingrate_L_DN.txt")))
ax8.plot(neuron(glob.glob("firingrate/firingrate_R_DN.txt")))
ax1.title.set_text('L017')
ax5.title.set_text('R017')
ax2.title.set_text('L112')
ax6.title.set_text('R112')
ax3.title.set_text('L153')
ax7.title.set_text('R153')
ax4.title.set_text('L_DN')
ax8.title.set_text('R_DN')
plt.xlabel('time(ms)')
plt.ylabel('Firingrate')
plt.savefig('figure/firingrate.png')

plot_place(neuron(glob.glob("firingrate/firingrate_DN_L.txt")),
			neuron(glob.glob("firingrate/firingrate_DN_R.txt")), goallist)



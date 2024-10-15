import iqif
import glob
import numpy as np
import math
import matplotlib.pyplot as plt
import time
from function import *


net = iqif.lifnet("parameter/neuronParameter_LIF.txt", "parameter/Connection_Table_LIF.txt")
#--------record-------------------------------------------------------------------------
neurons = [i for i in range(13)]
potential = {n: open(f"potential/potential_{n}.txt", "w") for n in neurons}
firingrate = {n: open(f"firingrate/firingrate_{n}.txt", "w") for n in neurons}
FR = [[0 for j in range(10)] for i in range(len(neurons))]
tmp_FR = [0 for i in range(len(neurons))]
#--------neuron parameters--------------------------------------------------------------

current = 0
cur_list = []
step = 0.01
for i in range(4000):
	net.set_biascurrent(0, current)
	net.send_synapse()
	current+=step
	for idx, n in enumerate(neurons):
		potential[n].write(f"{int(net.potential(idx))}\n")
	if((i+1)%10==0):
		cur_list.append(current)
		for idx, n in enumerate(neurons):
			tmp_FR[idx] = net.spike_count(idx)
		#print('tmp_FR = ', tmp_FR)	
		FR = update(FR,tmp_FR)
		for idx, n in enumerate(neurons):
			firingrate[n].write(f"{sum(FR[idx])}\n")
	
print("exit for loop")
for f in potential.values():
    f.close()
for f in firingrate.values():
	f.close()




fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
#ax3 = ax1.twinx()
ax1.plot(neuron(glob.glob("firingrate/firingrate_0.txt")), label = '0')
ax2.plot(cur_list, label = 'current')
fig.legend()
fig.tight_layout()
fig.savefig(f'IF_curve.png')





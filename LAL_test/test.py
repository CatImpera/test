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

for i in range(1000):
	for j in range(12):
		net.set_biascurrent(j, 15)
	net.send_synapse()
	for idx, n in enumerate(neurons):
		potential[n].write(f"{int(net.potential(idx))}\n")
	if((i+1)%10==0):
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



fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8)) = plt.subplots(2, 4, sharex=True, sharey=False)
fig.suptitle('potential')
#print(neuron(glob.glob("LAL/potential_L.txt")))
ax1.plot(neuron(glob.glob("potential/potential_0.txt")))
ax5.plot(neuron(glob.glob("potential/potential_1.txt")))
ax2.plot(neuron(glob.glob("potential/potential_2.txt")))
ax6.plot(neuron(glob.glob("potential/potential_3.txt")))
ax3.plot(neuron(glob.glob("potential/potential_4.txt")))
ax7.plot(neuron(glob.glob("potential/potential_5.txt")))
ax4.plot(neuron(glob.glob("potential/potential_6.txt")))
ax8.plot(neuron(glob.glob("potential/potential_12.txt")))

plt.xlabel('time(ms)')
plt.ylabel('v')
plt.savefig('figure/potential.png')

'''
plt.figure()
plt.plot(neuron(glob.glob("potential_L.txt")))
plt.show()
plt.close()
plt.plot(neuron(glob.glob("potential_R.txt")))
plt.show()
plt.plot(neuron(glob.glob("potential_EL.txt")))
plt.show()
plt.plot(neuron(glob.glob("potential_ER.txt")))
plt.show()
plt.plot(neuron(glob.glob("potential_IL.txt")))
plt.show()
plt.plot(neuron(glob.glob("potential_IR.txt")))
plt.show()
plt.plot(neuron(glob.glob("potential_DN_L.txt")))
plt.show()
plt.plot(neuron(glob.glob("potential_DN_R.txt")))
plt.show()
'''

for i in range(13):
	plt.figure()
	plt.plot(neuron(glob.glob(f"firingrate/firingrate_{i}.txt")))
	plt.savefig(f"firingrate_{i}.png")




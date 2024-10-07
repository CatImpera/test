import iqif
import glob
import numpy as np
import math
import matplotlib.pyplot as plt
import time
from function import *


time.sleep(3)
net = iqif.lifnet("parameter/neuronParameter_LIF.txt", "parameter/Connection_Table_LIF.txt")
#--------record-------------------------------------------------------------------------
neurons = ['L', 'R', 'EL', 'ER', 'IL', 'IR', 'DN_L', 'DN_R']
potential = {n: open(f"potential/potential_{n}.txt", "w") for n in neurons}
firingrate = {n: open(f"firingrate/firingrate_{n}.txt", "w") for n in neurons}
FR = [[0 for j in range(10)] for i in range(8)]
tmp_FR = [0 for i in range(8)]
#--------neuron parameters--------------------------------------------------------------
head = 171
goal = 182.5
slope = 0.2
var_y = 10
place = []
time_list = []
strength_list = []
fold = 0.02
strength = 0
t0 = time.time()
I_L = []
I_R = []
count = 25

for _ in range(500):
	if _<500:
		net.set_biascurrent(0, 25)
		net.set_biascurrent(1, 25)
		net.send_synapse()
	else:
		#if((_+1)%100==0):
		#	count-=1
		#	print("count = ", count)
		#net.set_biascurrent(0, count)
		#net.set_biascurrent(1, count)
		net.set_biascurrent(0, 15*1/(1+math.exp((head-goal)*slope))+var_y)
		net.set_biascurrent(1, 15*1/(1+math.exp(-(head-goal)*slope))+var_y)
		net.send_synapse()
	for idx, n in enumerate(neurons):
		potential[n].write(f"{int(net.potential(idx))}\n")
	pass
	if((_+1)%10==0):
		for idx, n in enumerate(neurons):
			tmp_FR[idx] = net.spike_count(idx)
		#print('tmp_FR = ', tmp_FR)	
		FR = update(FR,tmp_FR)
		for idx, n in enumerate(neurons):
			firingrate[n].write(f"{sum(FR[idx])}\n") 
	if((_+1)%10==0):
		#print('0 = ', 136*1/(1+math.exp((head-goal)*slope))+var_y)
		#print('1 = ', 136*1/(1+math.exp(-(head-goal)*slope))+var_y)
		#print("loop   place               turn  strength  direction")
		#print("{:<4}   {:<3}   ".format(_, head), end = "")
		left_motor = sum(FR[6])  #DN_L firingrate
		right_motor = sum(FR[7]) #DN_R firingrate
		turn = (right_motor-left_motor)*fold
		strength = turn_strength(abs(turn))
		#print("  {:<5}  {:1}        ".format(turn, strength), end = "")
		if turn>0:
			#print("->")
			if _>=300:
				head = head+0.02*strength
			#print("tmp = ","Right "+str(strength))
		elif turn<0:
			#print("<-")
			if _>=300:
				head = head-0.02*strength
		#else:
			#print("  ")
		#elif (abs(turn)<=0.02 and _>100):
		#	print('step 0')
		#	break
		place.append(head)
		time_list.append(time.time()-t0)
		strength_list.append(strength)
		I_L.append(136*1/(1+math.exp((head-goal)*slope))+var_y)
		I_R.append(136*1/(1+math.exp(-(head-goal)*slope))+var_y)
	#time.sleep(0.01)
print("exit for loop")
for f in potential.values():
    f.close()
for f in firingrate.values():
	f.close()

plt.figure()
plt.plot(neuron(glob.glob("potential/potential_L.txt")))
plt.savefig('potential_L.png')
plt.close()
'''
fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8)) = plt.subplots(2, 4, sharex=True, sharey=False)
fig.suptitle('potential')
#print(neuron(glob.glob("LAL/potential_L.txt")))
ax1.plot(neuron(glob.glob("potential/potential_L.txt")))
ax5.plot(neuron(glob.glob("potential/potential_R.txt")))
ax2.plot(neuron(glob.glob("potential/potential_EL.txt")))
ax6.plot(neuron(glob.glob("potential/potential_ER.txt")))
ax3.plot(neuron(glob.glob("potential/potential_IL.txt")))
ax7.plot(neuron(glob.glob("potential/potential_IR.txt")))
ax4.plot(neuron(glob.glob("potential/potential_DN_L.txt")))
ax8.plot(neuron(glob.glob("potential/potential_DN_R.txt")))
ax1.title.set_text('L')
ax5.title.set_text('R')
ax2.title.set_text('EL')
ax6.title.set_text('ER')
ax3.title.set_text('IL')
ax7.title.set_text('IR')
ax4.title.set_text('DN_L')
ax8.title.set_text('DN_R')
plt.xlabel('time(ms)')
plt.ylabel('v')
plt.savefig('figure/potential.png')
'''
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
'''
fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8)) = plt.subplots(2, 4, sharex=True, sharey=False)
fig.suptitle('potential')
ax1.plot(neuron(glob.glob("firingrate/firingrate_L.txt")))
#ax1.plot(I_L)
ax5.plot(neuron(glob.glob("firingrate/firingrate_R.txt")))
ax2.plot(neuron(glob.glob("firingrate/firingrate_EL.txt")))
ax6.plot(neuron(glob.glob("firingrate/firingrate_ER.txt")))
ax3.plot(neuron(glob.glob("firingrate/firingrate_IL.txt")))
ax7.plot(neuron(glob.glob("firingrate/firingrate_IR.txt")))
ax4.plot(neuron(glob.glob("firingrate/firingrate_DN_L.txt")))
ax8.plot(neuron(glob.glob("firingrate/firingrate_DN_R.txt")))
ax1.title.set_text('L')
ax5.title.set_text('R')
ax2.title.set_text('EL')
ax6.title.set_text('ER')
ax3.title.set_text('IL')
ax7.title.set_text('IR')
ax4.title.set_text('DN_L')
ax8.title.set_text('DN_R')
plt.xlabel('time(ms)')
plt.ylabel('Firingrate')
plt.savefig('figure/firingrate.png')

plt.figure()
plt.plot(neuron(glob.glob("firingrate/firingrate_L.txt")))
plt.plot(neuron(glob.glob("firingrate/firingrate_R.txt")))
plt.savefig("figure/firing_LR.png")
plt.close()

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
#ax3 = ax1.twinx()
tmp = neuron(glob.glob("firingrate/firingrate_DN_L.txt"))
ax1.plot([100*i for i in range(len(tmp))], tmp, label = 'DN_L')
tmp = neuron(glob.glob("firingrate/firingrate_DN_R.txt"))
ax1.plot([100*i for i in range(len(tmp))], tmp, label = 'DN_R')
ax2.plot([100*i for i in range(len(place))], place,marker = 'o', color = 'black', label = 'place')
#ax3.plot([100*i for i in range(len(I_R))], I_R, label = 'I_R')
#ax3.plot([100*i for i in range(len(I_L))], I_L, label = 'I_L')
ax2.axhline(goal, linestyle = '-')
fig.legend()
fig.tight_layout()
fig.savefig('figure/firingrate_DN.png')

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(time_list, place, color ='black', label = 'place')
ax1.set_ylim([173,181])
ax2.plot(time_list, strength_list,color ='tab:blue', label = 'strength')
ax1.axhline(goal, linestyle = '-')
fig.tight_layout()
fig.savefig('figure/place_strength.png')
'''


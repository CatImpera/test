import iqif
import glob
import numpy as np
import math
import matplotlib.pyplot as plt
import time
from function import *
import sys


###input angle
inp_g = 24#float(sys.argv[1])#14.5
inp_h = 32#float(sys.argv[2])#20
plot = True

goal_angle = [2,6,10,14,18,22,24,28,32,36,42,46]    #input range(12 - 36)
head_angle = [3, 9, 15, 21, 27, 33, 39, 45]     #input range(12-36)

goaln1 = 999999
goaln2 = 999999

headn1 = 999999
headn2 = 999999


#####goal#####
for k in range(0,11):
    if inp_g == goal_angle[k]:
        goaln1 = k
        break
    if inp_g == 46:
        goaln1=345
        break
    if inp_g > 46 or inp_g < 2:
        goaln1 = 11
        goaln2 = 0
        break
    if inp_g > goal_angle[k] and inp_g < goal_angle[k+1] :
        goaln1 = k
        goaln2 = k+1
        break


ratio_g = 0

#30 = 360/12
#48/12 = 4

if inp_g < 2:
    ratio_g = (inp_g+1)/4
elif inp_g > 46:
    ratio_g = (48-inp_g)/4
elif inp_g == 48:
    ratio_g = 0.5
elif goaln2 == 999999:
    ratio_g = 0
    goaln2 = goaln1
else:
    ratio_g = (inp_g-goal_angle[goaln1])/4

gIn1 = 1*(1-ratio_g)
gIn2 = 1*ratio_g

#####head#####


for k in range(0,7):
    if inp_h == head_angle[k]:
        headn1 = k
        break
    if inp_h > head_angle[k] and inp_h < head_angle[k+1] :
        headn1 = k
        headn2 = k+1
        break

ratio_h =0

#45 = 360/8
#48/8 = 6

if inp_h < 3:
    ratio_h = (inp_h+3)/6
elif inp_h > 45:
    ratio_h = (48-inp_h)/6
elif inp_h == 48:
    ratio_h = 0.5
elif headn2 == 999999:
    ratio_h = 0
    headn2 = headn1
else:
    ratio_h = (inp_h-head_angle[headn1])/6

hIn1 = 1*(1-ratio_h)
hIn2 = 1*ratio_h

goaln1 = goaln1+8
goaln2 = goaln2+8
"""
print("headn2 = ", headn2,"15*hIn2 = ", 15*hIn2)
print("headn1 = ", headn1,"15*hIn1 = ", 15*hIn1)
print("goaln2 = ", goaln2,"15*gIn2 = ", 15*gIn2)
print("goaln1 = ", goaln1,"15*gIn1 = ", 15*gIn1)
"""

net = iqif.lifnet("parameter/neuronParameter_LIF.txt", "parameter/Connection_Table_LIF.txt")
inhead_list = [f"inhead_{inhead}" for inhead in range(8)]
ingoal_list = [f"ingoal_{ingoal}" for ingoal in range(12)]
inheadin_list = ["inheadin_0"]
ingoalin_list = ["ingoalin_0"]
FC2_list = [f"FC2_{FC2}" for FC2 in range(12)]
headinput_list = [f"headinput_{headinput}" for headinput in range(16)]
PFL3_list = [f"PFL3_{PFL3}" for PFL3 in range(24)]
neu_list = inhead_list+ingoal_list+inheadin_list+ingoalin_list+FC2_list+headinput_list+PFL3_list
potential = {n: open(f"potential/potential_{n}.txt", "w") for n in neu_list}
firingrate = {n: open(f"firingrate/firingrate_{n}.txt", "w") for n in neu_list}
FR_list = [[0 for j in range(10)] for i in range(len(neu_list))]
tmp_FR = [0 for i in range(len(neu_list))]
time = 20000

print(headn1, 15*hIn1)
print(headn2, 15*hIn2)
print(goaln1, 15*gIn1)
print(goaln2, 15*gIn2)
for i in range(time):
	net.set_biascurrent(headn2, 15*hIn2)
	net.set_biascurrent(headn1, 15*hIn1)
	net.set_biascurrent(goaln2, 15*gIn2)
	net.set_biascurrent(goaln1, 15*gIn1)
	for idx, n in enumerate(neu_list):
		potential[n].write(f"{int(net.potential(idx))}\n")
	if((i+1)%10==0):
		for idx, n in enumerate(neu_list):
			tmp_FR[idx] = net.spike_count(idx)
		#print('tmp_FR = ', tmp_FR)	
		FR_list = update(FR_list,tmp_FR)
		for idx, n in enumerate(neu_list):
			firingrate[n].write(f"{sum(FR_list[idx])}\n")

for f in potential.values():
    f.close()
for f in firingrate.values():
    f.close()
    
if plot:
	fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8)) = plt.subplots(2, 4, sharex=True, sharey=False)
	fig.suptitle('potential')
	ax1.plot(neuron(glob.glob("potential/potential_inhead_0.txt")))
	ax2.plot(neuron(glob.glob("potential/potential_inhead_1.txt")))
	ax3.plot(neuron(glob.glob("potential/potential_inhead_2.txt")))
	ax4.plot(neuron(glob.glob("potential/potential_inhead_3.txt")))
	ax5.plot(neuron(glob.glob("potential/potential_inhead_4.txt")))
	ax6.plot(neuron(glob.glob("potential/potential_inhead_5.txt")))
	ax7.plot(neuron(glob.glob("potential/potential_inhead_6.txt")))
	ax8.plot(neuron(glob.glob("potential/potential_inhead_7.txt")))
	plt.xlabel('time(ms)')
	plt.ylabel('v')
	plt.savefig('figure/potential_head.png')

	fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8)) = plt.subplots(2, 4, sharex=True, sharey=False)
	fig.suptitle('potential')
	ax1.plot(neuron(glob.glob("potential/potential_ingoal_0.txt")))
	ax2.plot(neuron(glob.glob("potential/potential_ingoal_1.txt")))
	ax3.plot(neuron(glob.glob("potential/potential_ingoal_2.txt")))
	ax4.plot(neuron(glob.glob("potential/potential_ingoal_3.txt")))
	ax5.plot(neuron(glob.glob("potential/potential_ingoal_4.txt")))
	ax6.plot(neuron(glob.glob("potential/potential_ingoal_5.txt")))
	ax7.plot(neuron(glob.glob("potential/potential_ingoal_6.txt")))
	ax8.plot(neuron(glob.glob("potential/potential_ingoal_7.txt")))
	plt.xlabel('time(ms)')
	plt.ylabel('v')
	plt.savefig('figure/potential_goal.png')

	fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8)) = plt.subplots(2, 4, sharex=True, sharey=False)
	fig.suptitle('potential')
	ax1.plot(neuron(glob.glob("potential/potential_FC2_0.txt")))
	ax2.plot(neuron(glob.glob("potential/potential_FC2_1.txt")))
	ax3.plot(neuron(glob.glob("potential/potential_FC2_2.txt")))
	ax4.plot(neuron(glob.glob("potential/potential_FC2_3.txt")))
	ax5.plot(neuron(glob.glob("potential/potential_FC2_4.txt")))
	ax6.plot(neuron(glob.glob("potential/potential_FC2_5.txt")))
	ax7.plot(neuron(glob.glob("potential/potential_FC2_6.txt")))
	ax8.plot(neuron(glob.glob("potential/potential_FC2_7.txt")))
	plt.xlabel('time(ms)')
	plt.ylabel('v')
	plt.savefig('figure/potential_FC2.png')

	plt.figure()
	plt.plot(neuron(glob.glob("firingrate/firingrate_inhead_0.txt")))
	plt.plot(neuron(glob.glob("firingrate/firingrate_inhead_1.txt")))
	plt.plot(neuron(glob.glob("firingrate/firingrate_inhead_2.txt")))
	plt.plot(neuron(glob.glob("firingrate/firingrate_inhead_3.txt")))
	plt.plot(neuron(glob.glob("firingrate/firingrate_inhead_4.txt")))
	plt.plot(neuron(glob.glob("firingrate/firingrate_inhead_5.txt")))
	plt.plot(neuron(glob.glob("firingrate/firingrate_inhead_6.txt")))
	plt.plot(neuron(glob.glob("firingrate/firingrate_inhead_7.txt")))
	plt.xlabel('time(ms)')
	plt.ylabel('v')
	plt.savefig('figure/firingrate_head.png')

	plt.figure()
	#print('len = ', len(neuron(glob.glob("firingrate/firingrate_inhead_8.txt"))))
	plt.plot(neuron(glob.glob("firingrate/firingrate_ingoal_0.txt")))
	plt.plot(neuron(glob.glob("firingrate/firingrate_ingoal_1.txt")))
	plt.plot(neuron(glob.glob("firingrate/firingrate_ingoal_2.txt")))
	plt.plot(neuron(glob.glob("firingrate/firingrate_ingoal_3.txt")))
	plt.plot(neuron(glob.glob("firingrate/firingrate_ingoal_4.txt")))
	plt.plot(neuron(glob.glob("firingrate/firingrate_ingoal_5.txt")))
	plt.plot(neuron(glob.glob("firingrate/firingrate_ingoal_6.txt")))
	plt.plot(neuron(glob.glob("firingrate/firingrate_ingoal_7.txt")))
	plt.plot(neuron(glob.glob("firingrate/firingrate_ingoal_8.txt")))
	plt.plot(neuron(glob.glob("firingrate/firingrate_ingoal_9.txt")))
	plt.plot(neuron(glob.glob("firingrate/firingrate_ingoal_10.txt")))
	plt.plot(neuron(glob.glob("firingrate/firingrate_ingoal_11.txt")))
	plt.xlabel('time(ms)')
	plt.ylabel('v')
	plt.savefig('figure/firingrate_goal.png')


	plt.figure()
	plt.bar(0,neuron(glob.glob("firingrate/firingrate_inhead_0.txt"))[int(time/10)-1])
	plt.bar(1,neuron(glob.glob("firingrate/firingrate_inhead_1.txt"))[int(time/10)-1])
	plt.bar(2,neuron(glob.glob("firingrate/firingrate_inhead_2.txt"))[int(time/10)-1])
	plt.bar(3,neuron(glob.glob("firingrate/firingrate_inhead_3.txt"))[int(time/10)-1])
	plt.bar(4,neuron(glob.glob("firingrate/firingrate_inhead_4.txt"))[int(time/10)-1])
	plt.bar(5,neuron(glob.glob("firingrate/firingrate_inhead_5.txt"))[int(time/10)-1])
	plt.bar(6,neuron(glob.glob("firingrate/firingrate_inhead_6.txt"))[int(time/10)-1])
	plt.bar(7,neuron(glob.glob("firingrate/firingrate_inhead_7.txt"))[int(time/10)-1])

	plt.xlabel('neuron index')
	plt.ylabel('r')
	plt.savefig('figure/trace_inhead.png')
	
	plt.figure()
	plt.bar(0,neuron(glob.glob("firingrate/firingrate_inheadin_0.txt"))[int(time/10)-1])

	plt.xlabel('neuron index')
	plt.ylabel('r')
	plt.savefig('figure/trace_inheadin.png')
	
	plt.figure()
	plt.plot(neuron(glob.glob("potential/potential_inheadin_0.txt")))

	plt.xlabel('neuron index')
	plt.ylabel('r')
	plt.savefig('figure/potential_inheadin.png')

	plt.figure()
	#print(neuron(glob.glob("firingrate/firingrate_inhead_0.txt")))
	plt.bar(0,neuron(glob.glob("firingrate/firingrate_ingoal_0.txt"))[int(time/10)-1])
	plt.bar(1,neuron(glob.glob("firingrate/firingrate_ingoal_1.txt"))[int(time/10)-1])
	plt.bar(2,neuron(glob.glob("firingrate/firingrate_ingoal_2.txt"))[int(time/10)-1])
	plt.bar(3,neuron(glob.glob("firingrate/firingrate_ingoal_3.txt"))[int(time/10)-1])
	plt.bar(4,neuron(glob.glob("firingrate/firingrate_ingoal_4.txt"))[int(time/10)-1])
	plt.bar(5,neuron(glob.glob("firingrate/firingrate_ingoal_5.txt"))[int(time/10)-1])
	plt.bar(6,neuron(glob.glob("firingrate/firingrate_ingoal_6.txt"))[int(time/10)-1])
	plt.bar(7,neuron(glob.glob("firingrate/firingrate_ingoal_7.txt"))[int(time/10)-1])
	plt.bar(8,neuron(glob.glob("firingrate/firingrate_ingoal_8.txt"))[int(time/10)-1])
	plt.bar(9,neuron(glob.glob("firingrate/firingrate_ingoal_9.txt"))[int(time/10)-1])
	plt.bar(10,neuron(glob.glob("firingrate/firingrate_ingoal_10.txt"))[int(time/10)-1])
	plt.bar(11,neuron(glob.glob("firingrate/firingrate_ingoal_11.txt"))[int(time/10)-1])

	plt.xlabel('neuron index')
	plt.ylabel('r')
	plt.savefig('figure/trace_ingoal.png')

	plt.figure()
	plt.bar(0,neuron(glob.glob("firingrate/firingrate_FC2_0.txt"))[int(time/10)-1])
	plt.bar(1,neuron(glob.glob("firingrate/firingrate_FC2_1.txt"))[int(time/10)-1])
	plt.bar(2,neuron(glob.glob("firingrate/firingrate_FC2_2.txt"))[int(time/10)-1])
	plt.bar(3,neuron(glob.glob("firingrate/firingrate_FC2_3.txt"))[int(time/10)-1])
	plt.bar(4,neuron(glob.glob("firingrate/firingrate_FC2_4.txt"))[int(time/10)-1])
	plt.bar(5,neuron(glob.glob("firingrate/firingrate_FC2_5.txt"))[int(time/10)-1])
	plt.bar(6,neuron(glob.glob("firingrate/firingrate_FC2_6.txt"))[int(time/10)-1])
	plt.bar(7,neuron(glob.glob("firingrate/firingrate_FC2_7.txt"))[int(time/10)-1])
	plt.bar(8,neuron(glob.glob("firingrate/firingrate_FC2_8.txt"))[int(time/10)-1])
	plt.bar(9,neuron(glob.glob("firingrate/firingrate_FC2_9.txt"))[int(time/10)-1])
	plt.bar(10,neuron(glob.glob("firingrate/firingrate_FC2_10.txt"))[int(time/10)-1])
	plt.bar(11,neuron(glob.glob("firingrate/firingrate_FC2_11.txt"))[int(time/10)-1])

	plt.xlabel('neuron index')
	plt.ylabel('r')
	plt.savefig('figure/trace_FC2.png')


	plt.figure()
	plt.bar(0,neuron(glob.glob("firingrate/firingrate_headinput_0.txt"))[int(time/10)-1])
	plt.bar(1,neuron(glob.glob("firingrate/firingrate_headinput_1.txt"))[int(time/10)-1])
	plt.bar(2,neuron(glob.glob("firingrate/firingrate_headinput_2.txt"))[int(time/10)-1])
	plt.bar(3,neuron(glob.glob("firingrate/firingrate_headinput_3.txt"))[int(time/10)-1])
	plt.bar(4,neuron(glob.glob("firingrate/firingrate_headinput_4.txt"))[int(time/10)-1])
	plt.bar(5,neuron(glob.glob("firingrate/firingrate_headinput_5.txt"))[int(time/10)-1])
	plt.bar(6,neuron(glob.glob("firingrate/firingrate_headinput_6.txt"))[int(time/10)-1])
	plt.bar(7,neuron(glob.glob("firingrate/firingrate_headinput_7.txt"))[int(time/10)-1])
	plt.bar(8,neuron(glob.glob("firingrate/firingrate_headinput_8.txt"))[int(time/10)-1])
	plt.bar(9,neuron(glob.glob("firingrate/firingrate_headinput_9.txt"))[int(time/10)-1])
	plt.bar(10,neuron(glob.glob("firingrate/firingrate_headinput_10.txt"))[int(time/10)-1])
	plt.bar(11,neuron(glob.glob("firingrate/firingrate_headinput_11.txt"))[int(time/10)-1])
	plt.bar(12,neuron(glob.glob("firingrate/firingrate_headinput_12.txt"))[int(time/10)-1])
	plt.bar(13,neuron(glob.glob("firingrate/firingrate_headinput_13.txt"))[int(time/10)-1])
	plt.bar(14,neuron(glob.glob("firingrate/firingrate_headinput_14.txt"))[int(time/10)-1])
	plt.bar(15,neuron(glob.glob("firingrate/firingrate_headinput_15.txt"))[int(time/10)-1])

	plt.xlabel('neuron index')
	plt.ylabel('r')
	plt.savefig('figure/trace_headinput.png')

	plt.figure()
	plt.bar(0,neuron(glob.glob("firingrate/firingrate_PFL3_0.txt"))[int(time/10)-1],color='red')
	plt.bar(1,neuron(glob.glob("firingrate/firingrate_PFL3_1.txt"))[int(time/10)-1],color='blue')
	plt.bar(2,neuron(glob.glob("firingrate/firingrate_PFL3_2.txt"))[int(time/10)-1],color='red')
	plt.bar(3,neuron(glob.glob("firingrate/firingrate_PFL3_3.txt"))[int(time/10)-1],color='blue')
	plt.bar(4,neuron(glob.glob("firingrate/firingrate_PFL3_4.txt"))[int(time/10)-1],color='red')
	plt.bar(5,neuron(glob.glob("firingrate/firingrate_PFL3_5.txt"))[int(time/10)-1],color='blue')
	plt.bar(6,neuron(glob.glob("firingrate/firingrate_PFL3_6.txt"))[int(time/10)-1],color='red')
	plt.bar(7,neuron(glob.glob("firingrate/firingrate_PFL3_7.txt"))[int(time/10)-1],color='blue')
	plt.bar(8,neuron(glob.glob("firingrate/firingrate_PFL3_8.txt"))[int(time/10)-1],color='red')
	plt.bar(9,neuron(glob.glob("firingrate/firingrate_PFL3_9.txt"))[int(time/10)-1],color='blue')
	plt.bar(10,neuron(glob.glob("firingrate/firingrate_PFL3_10.txt"))[int(time/10)-1],color='red')
	plt.bar(11,neuron(glob.glob("firingrate/firingrate_PFL3_11.txt"))[int(time/10)-1],color='blue')
	plt.bar(12,neuron(glob.glob("firingrate/firingrate_PFL3_12.txt"))[int(time/10)-1],color='red')
	plt.bar(13,neuron(glob.glob("firingrate/firingrate_PFL3_13.txt"))[int(time/10)-1],color='blue')
	plt.bar(14,neuron(glob.glob("firingrate/firingrate_PFL3_14.txt"))[int(time/10)-1],color='red')
	plt.bar(15,neuron(glob.glob("firingrate/firingrate_PFL3_15.txt"))[int(time/10)-1],color='blue')
	plt.bar(16,neuron(glob.glob("firingrate/firingrate_PFL3_16.txt"))[int(time/10)-1],color='red')
	plt.bar(17,neuron(glob.glob("firingrate/firingrate_PFL3_17.txt"))[int(time/10)-1],color='blue')
	plt.bar(18,neuron(glob.glob("firingrate/firingrate_PFL3_18.txt"))[int(time/10)-1],color='red')
	plt.bar(19,neuron(glob.glob("firingrate/firingrate_PFL3_19.txt"))[int(time/10)-1],color='blue')
	plt.bar(20,neuron(glob.glob("firingrate/firingrate_PFL3_20.txt"))[int(time/10)-1],color='red')
	plt.bar(21,neuron(glob.glob("firingrate/firingrate_PFL3_21.txt"))[int(time/10)-1],color='blue')
	plt.bar(22,neuron(glob.glob("firingrate/firingrate_PFL3_22.txt"))[int(time/10)-1],color='red')
	plt.bar(23,neuron(glob.glob("firingrate/firingrate_PFL3_23.txt"))[int(time/10)-1],color='blue')

	plt.xlabel('neuron index')
	plt.ylabel('r')
	plt.savefig('figure/trace_PFL3.png')

L = 0
R = 0
L+=neuron(glob.glob("firingrate/firingrate_PFL3_0.txt"))[int(time/10)-1]
R+=neuron(glob.glob("firingrate/firingrate_PFL3_1.txt"))[int(time/10)-1]
L+=neuron(glob.glob("firingrate/firingrate_PFL3_2.txt"))[int(time/10)-1]
R+=neuron(glob.glob("firingrate/firingrate_PFL3_3.txt"))[int(time/10)-1]
L+=neuron(glob.glob("firingrate/firingrate_PFL3_4.txt"))[int(time/10)-1]
R+=neuron(glob.glob("firingrate/firingrate_PFL3_5.txt"))[int(time/10)-1]
L+=neuron(glob.glob("firingrate/firingrate_PFL3_6.txt"))[int(time/10)-1]
R+=neuron(glob.glob("firingrate/firingrate_PFL3_7.txt"))[int(time/10)-1]
L+=neuron(glob.glob("firingrate/firingrate_PFL3_8.txt"))[int(time/10)-1]
R+=neuron(glob.glob("firingrate/firingrate_PFL3_9.txt"))[int(time/10)-1]
L+=neuron(glob.glob("firingrate/firingrate_PFL3_10.txt"))[int(time/10)-1]
R+=neuron(glob.glob("firingrate/firingrate_PFL3_11.txt"))[int(time/10)-1]
L+=neuron(glob.glob("firingrate/firingrate_PFL3_12.txt"))[int(time/10)-1]
R+=neuron(glob.glob("firingrate/firingrate_PFL3_13.txt"))[int(time/10)-1]
L+=neuron(glob.glob("firingrate/firingrate_PFL3_14.txt"))[int(time/10)-1]
R+=neuron(glob.glob("firingrate/firingrate_PFL3_15.txt"))[int(time/10)-1]
L+=neuron(glob.glob("firingrate/firingrate_PFL3_16.txt"))[int(time/10)-1]
R+=neuron(glob.glob("firingrate/firingrate_PFL3_17.txt"))[int(time/10)-1]
L+=neuron(glob.glob("firingrate/firingrate_PFL3_18.txt"))[int(time/10)-1]
R+=neuron(glob.glob("firingrate/firingrate_PFL3_19.txt"))[int(time/10)-1]
L+=neuron(glob.glob("firingrate/firingrate_PFL3_20.txt"))[int(time/10)-1]
R+=neuron(glob.glob("firingrate/firingrate_PFL3_21.txt"))[int(time/10)-1]
L+=neuron(glob.glob("firingrate/firingrate_PFL3_22.txt"))[int(time/10)-1]
R+=neuron(glob.glob("firingrate/firingrate_PFL3_23.txt"))[int(time/10)-1]

print("L = ",L)
print("R = ",R)

"""
fig = plt.figure()
ax = plt.axes(projection='3d')
D_inhead = []
D_inhead.append(neuron(glob.glob("firingrate/firingrate_inhead_0.txt")))
D_inhead.append(neuron(glob.glob("firingrate/firingrate_inhead_1.txt")))
D_inhead.append(neuron(glob.glob("firingrate/firingrate_inhead_2.txt")))
D_inhead.append(neuron(glob.glob("firingrate/firingrate_inhead_3.txt")))
D_inhead.append(neuron(glob.glob("firingrate/firingrate_inhead_4.txt")))
D_inhead.append(neuron(glob.glob("firingrate/firingrate_inhead_5.txt")))
D_inhead.append(neuron(glob.glob("firingrate/firingrate_inhead_6.txt")))
D_inhead.append(neuron(glob.glob("firingrate/firingrate_inhead_7.txt")))
D_inhead = np.array(D_inhead)
x = [0,1,2,3,4,5,6,7]
y = [i for i in range(int(time/10))]
rows, cols = np.shape(D_inhead)
print(len(y))
X, Y = np.meshgrid(range(cols), range(rows))

ax.plot_wireframe(X,Y,D_inhead)
plt.ion()
plt.show()
plt.savefig("3D.png")
plt.close()
"""

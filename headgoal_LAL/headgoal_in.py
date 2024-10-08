import iqif
import glob
import numpy as np
import math
import matplotlib.pyplot as plt
import time
from function import *
import sys

def inputgoal(goalplace):

	inp_g = goalplace
	
	goal_angle = [2,6,10,14,18,22,26,30,34,38,42,46]    #input range(12 - 36)
	
	goaln1 = 999999
	goaln2 = 999999
	
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
	else:
		ratio_g = (inp_g-goal_angle[goaln1])/4

	gIn1 = 1*(1-ratio_g)
	gIn2 = 1*ratio_g
	
	
	return goaln1, goaln2, gIn1, gIn2

goal = 12
list1 = []
list2 = []
for i in range(240):
	goaln1, goaln2, gIn1, gIn2 = inputgoal(round(goal,2))
	list1.append(gIn1)
	list2.append(gIn2)
	goal+=0.1
plt.figure()
plt.plot(list1)
plt.plot(list2)
plt.savefig('input.png')
plt.close()

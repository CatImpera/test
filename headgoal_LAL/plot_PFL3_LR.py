import iqif
import glob
import numpy as np
import math
import matplotlib.pyplot as plt
import time
from function import *
import sys

L = []
R = []
with open("L.txt","r") as f:
	lines = f.readlines()
	for line in lines:
		L.append(int(line))
		
with open("R.txt","r") as f:
	lines = f.readlines()
	for line in lines:
		R.append(int(line))
		
#for i in range(len(L)):
#	L[i] = L[i]-R[i]
fig,ax = plt.subplots()
x_ticks = [i for i in range(13,36)]
ax.plot(list(np.arange(13, 35.5, 0.5)),L)
ax.plot(list(np.arange(13, 35.5, 0.5)),R)
plt.grid(True)

plt.xticks(x_ticks)
ax.xaxis.grid(linestyle = '--' ,linewidth =1 ,alpha =0.3 )
plt.savefig("plot_PFL3_LR.png")
plt.close()

for i in range(len(L)):
	L[i] = L[i]-R[i]
plt.figure()
plt.plot(L)
plt.savefig("plot_PFL3_LR_dis.png")
plt.close()

